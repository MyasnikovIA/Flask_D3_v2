import datetime
import os
import shutil
import json
import uuid
from pathlib import Path
from flask import Flask, redirect, session, render_template, request, g
import getform
import requests as req
import urllib.parse
import random

from Etc.conf import ConfigOptions
from System.d3main import show as d3main_js
from System.d3theme import show as d3theme_css
app = Flask(__name__, static_folder='templates')
app.secret_key = str(uuid.uuid1()).replace("-", "")
app.config['CORS_HEADERS'] = 'Content-Type'
app.permanent_session_lifetime = datetime.timedelta(days=10)  # период хронений сессии составляет 10 дней


def sendCostumBin(pathFile):
    # костыль для docker
    txt = ""
    if getform.existTempPage(pathFile):
        txt, mime = getform.getTempPage(pathFile, '')
    if txt == "":
        if os.path.isfile(pathFile):
            with open(pathFile, "rb") as f:
                return f.read(), getform.mimeType(pathFile)
        else:
            # fpath = Path(__file__).absolute()
            fpath = os.path.dirname(Path(__file__).absolute())
            return f"File {pathFile} not found {os.path.dirname(Path(__file__).absolute())}{os.sep}  --{fpath}---", getform.mimeType(
                ".txt")
    else:
        return txt, mime


@app.before_request
def before_request():
    """
    Функция запускается перед запросом
    Добавляет соединение к БД
    """
    pass


@app.after_request
def after_request(response):
    # CORS in flask
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    header['Server'] = 'D3apiServer'
    return response

# @app.errorhandler(404)
# def not_found(error):
#   return app.send_static_file('/templates/404.html'), 404
#   return render_template('404.html', **locals()), 404

@app.route('/')
def example():
    # user_agent = request.headers.get('User-Agent')
    # return app.send_static_file('index.html')
    return redirect("/index.html")

def getParam(name, defoultValue=''):
    return request.args.get(name, default=defoultValue)

countQuery = 0
@app.route('/<path:path>', methods=['GET', 'POST'])
def all_files(path):
    if session.get("ID") == None:
        global countQuery
        countQuery += 1
        session["ID"] = f'{str(uuid.uuid1()).replace("-", "")}{countQuery}{datetime.datetime.now().microsecond}'
    ext = path[path.rfind('.') + 1:].lower()
    """
    try:
        # Инициализация информации об агенте()
        if ext in ["html", "css", ".js"]:
            getform.getAgentInfo(request)
    except:
        pass
    """
    ROOT_DIR = f"{os.path.dirname(Path(__file__).absolute())}{os.sep}"
    ROOT_FORM_DIR = f"{os.path.dirname(Path(__file__).absolute())}{os.sep}Forms{os.sep}"
    if '/~Cmp' in path and 'Components/' in path:
        cmp = path[path.find('Components/') + len('Components/'): path.find('/~Cmp') - len('/~Cmp') + 1]
        img = path[path.rfind("/"):]
        pathImg = f"{ROOT_DIR}Components/{cmp}/images/default{img}.png"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if 'Components/' in path:
        pathImg = f"{ROOT_DIR}{path[path.find('Components/'):]}"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if 'favicon.ico' in path:
        pathImg = f"{ROOT_DIR}{path}"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if "~d3theme" in path:
        return d3theme_css(request), 200, {'content-type': 'text/css'}

    if "~d3main" in path:
        return d3main_js(request), 200, {'content-type': 'application/x-javascript'}

    if "getform.php" in path:
        formName = getParam('Form')
        if "http" in formName or  "https" in formName:
            # Дописать авторизацию на удаленном сервере
            o = urllib.parse.urlsplit(formName)
            # o.hostname # адрес сервера
            # o.path # путь к форме
            # o.query # параметры ключ=значение  в URL строке
            htmlResObj = req.get(formName)
            frm = htmlResObj.content
        else:
            cache = getParam('cache')
            dataSetName = getParam('DataSet', "")
            frm = getform.getParsedForm(formName, cache, dataSetName, session)
        return frm, 200, {'content-type': 'application/plain'}

    if "request.php" in path:
        resultTxt = "{}"
        formName = getParam('Form')
        cache = getParam('cache')
        if request.method == 'POST':
            dataSet = json.loads(request.form.get('request'))
            for dataSetName in dataSet:
                typeQuery = dataSet[dataSetName]["type"]
                paramsQuery = dataSet[dataSetName]["params"]
                if len(formName) == 0:
                    formName = urllib.parse.urlsplit(request.referrer).path[1:]
                resultTxt = getform.dataSetQuery(f'{formName}:{dataSetName}', typeQuery, paramsQuery, session)
                # getRunAction(formName, cache, name, queryActionObject[name])
        return resultTxt, 200, {'Content-Type': 'text/xml; charset=utf-8'}

    # Поиск запроса в каталоге форм
    pathHtmlFromForm = f"{ROOT_FORM_DIR}{path}"
    if os.path.isfile(pathHtmlFromForm):
        cache = getParam('cache')
        dataSetName = getParam('DataSet', "")
        if ext == "frm":
            frm = getform.getParsedForm(path, cache, dataSetName, session)
            return frm, 200, {'content-type': 'text/html'}
        else:
            frm = getform.getParsedForm(path, cache, dataSetName, session)
            return frm, 200, {'content-type': 'text/html'}

    if path[-3:].lower() in ["tml", "htm"]:
        return redirect("/index.html")
    return render_template('404.html', **locals()), 404
    # return app.render_template(path)
    # return app.send_static_file(path)


if __name__ == '__main__':
    if "debug" in ConfigOptions and not int(ConfigOptions["debug"]) == 0:
        TEMP_DIR_PATH = os.path.join(os.path.dirname(Path(__file__).absolute()), ConfigOptions['TempDir'])
        if os.path.exists(TEMP_DIR_PATH):
            for root, dirs, files in os.walk(TEMP_DIR_PATH):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
        else:
            os.mkdir(TEMP_DIR_PATH)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)


"""
заметки
>>> import urllib.parse
>>> o = urllib.parse.urlsplit('https://user:pass@www.example.com:8080/dir/page.html?q1=test&q2=a2#anchor1')
>>> o.scheme
'https'
>>> o.netloc
'user:pass@www.example.com:8080'
>>> o.hostname
'www.example.com'
>>> o.port
8080
>>> o.path
'/dir/page.html'
>>> o.query
'q1=test&q2=a2'
>>> o.fragment
'anchor1'
>>> o.username
'user'
>>> o.password
'pass'

"""