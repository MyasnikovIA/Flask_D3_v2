import datetime
import os
import sys
import shutil
import json
import uuid
from pathlib import Path
from flask import Flask
from flask import redirect
from flask import session
from flask import render_template
from flask import request
import getform
import requests as reqExt
import urllib.parse

from System.d3main import show as d3main_js
from System.d3theme import show as d3theme_css
app = Flask(__name__, static_folder='templates')
app.secret_key = str(uuid.uuid1()).replace("-", "")
app.config['CORS_HEADERS'] = 'Content-Type'
app.permanent_session_lifetime = datetime.timedelta(days=10)  # период хронений сессии составляет 10 дней


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
    header['Access-Control-Allow-Origin'] = '*'  # https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    header['Access-Control-Allow-Headers'] = '*' # https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Access-Control-Allow-Headers
    header['Access-Control-Allow-Methods'] = '*' # https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Access-Control-Allow-Methods
    header['Server'] = 'D3apiServer'
    return response

@app.route('/')
def example():
    return redirect("/index.html")


def getParam(name, defoultValue=''):
    return request.args.get(name, default=defoultValue)

countQuery = 0
@app.route('/<path:path>', methods=['GET', 'POST'])
def all_files(path):

    # инициализируем
    if session.get("ID") == None:
        global countQuery
        countQuery += 1
        session["ID"] = f'{str(uuid.uuid1()).replace("-", "")}{countQuery}{datetime.datetime.now().microsecond}'
        getform.REMOTE_SESSION_DICT[session["ID"]] = {}
    ext = path[path.rfind('.') + 1:].lower()
    getform.getAgentInfo(session,request) # получить информацию о клиенте
    ROOT_DIR = f"{os.path.dirname(Path(__file__).absolute())}{os.sep}"
    #ROOT_FORM_DIR = f"{os.path.dirname(Path(__file__).absolute())}{os.sep}Forms{os.sep}"

    # Получение контента с использованием в пути псевдонима  /~Cmp (наследие из PHP)
    if '/~Cmp' in path and 'Components/' in path:
        cmp = path[path.find('Components/') + len('Components/'): path.find('/~Cmp') - len('/~Cmp') + 1]
        img = path[path.rfind("/"):]
        pathImg = f"{ROOT_DIR}Components/{cmp}/images/default{img}.png"
        bin, mime = getform.sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    #  Получение контента для компонентов
    if 'Components/' in path:
        pathImg = f"{ROOT_DIR}{path[path.find('Components/'):]}"
        bin, mime = getform.sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    # Получение иконки страницы
    if 'favicon.ico' in path:
        pathImg = f"{ROOT_DIR}{path}"
        bin, mime = getform.sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    # Получение CSS библиотеки платформы D3Ext
    if "~d3theme" in path:
        return d3theme_css(request), 200, {'content-type': 'text/css; charset=utf-8'}

    # Получение JS библиотеки платформы D3Ext
    if "~d3main" in path:
        return d3main_js(request), 200, {'content-type': 'application/x-javascript; charset=utf-8'}

    # Получение пользовательских форм описанных в формате XML
    if "getform.php" in path:
        formName = getParam('Form')
        external = getParam('external','');
        extSub = formName[formName.rfind('.') + 1:].lower()
        if "http" in formName or  "https" in formName:
            if not extSub == 'html' and not extSub == 'frm':
                formName=f"{formName}.frm"
            urlParstmp = urllib.parse.urlsplit(formName)
            if urlParstmp.hostname in getform.REMOTE_SESSION_DICT[session["ID"]]:
                remote_session = getform.REMOTE_SESSION_DICT[session["ID"]][urlParstmp.hostname]
            else:
                remote_session = reqExt.Session()
                getform.REMOTE_SESSION_DICT[session["ID"]][urlParstmp.hostname] = remote_session
            htmlResObj = remote_session.get(f"{formName}?REMOUTE=1")
            frm = htmlResObj.content
        else:
            cache = getParam('cache')
            dataSetName = getParam('DataSet', "")
            frm = getform.getParsedForm(formName, cache, dataSetName, session)
        return frm, 200, {'content-type': 'application/plain; charset=utf-8'}

    # Обработка запросов DataSet Action
    if "request.php" in path:
        resultTxt = "{}"
        formName = getParam('Form')
        cache = getParam('cache')
        requestPoetText = request.form.get('request')
        if not requestPoetText:
            requestPoetText = request.data.decode()
        dataSet = json.loads(requestPoetText)
        if request.method == 'POST':
            extSub = formName[formName.rfind('.') + 1:].lower()
            if "http" in formName or  "https" in formName:
                    if not extSub == 'html' and not extSub == 'frm':
                        formName=f"{formName}"
                    urlParstmp = urllib.parse.urlsplit(formName)
                    if urlParstmp.hostname in getform.REMOTE_SESSION_DICT[session["ID"]]:
                        remote_session = getform.REMOTE_SESSION_DICT[session["ID"]][urlParstmp.hostname]
                    else:
                        remote_session = reqExt.Session()
                        getform.REMOTE_SESSION_DICT[session["ID"]][urlParstmp.hostname] = remote_session
                    remote_headers_query = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                    url_tmp = f"{urlParstmp.scheme}://{urlParstmp.netloc}/request.php?cache_enabled=0&REMOUTE=1&Form={urlParstmp.path[1:]}"
                    result_query = remote_session.post(url_tmp, headers=remote_headers_query,json=dataSet)
                    resultTxt = result_query.text
            else:
                for dataSetName in dataSet:
                    typeQuery = dataSet[dataSetName]["type"]
                    paramsQuery = dataSet[dataSetName]["params"]
                    if len(formName) == 0:
                        formName = urllib.parse.urlsplit(request.referrer).path[1:]
                    resultTxt = getform.dataSetQuery(f'{formName}:{dataSetName}', typeQuery, paramsQuery, session)
                    # getRunAction(formName, cache, name, queryActionObject[name])
        return resultTxt, 200, {'Content-Type': 'text/xml; charset=utf-8'}


    # Поиск запроса в каталоге форм
    pathHtmlFromForm = f"{getform.FORM_PATH}{os.sep}{path}"
    if os.path.isfile(pathHtmlFromForm):
        cache = getParam('cache')
        dataSetName = getParam('DataSet', "")
        if ext == "frm":
            frm = getform.getParsedForm(path, cache, dataSetName, session)
            return frm, 200, {'content-type': 'text/html; charset=utf-8'}
        else:
            frm = getform.getParsedForm(path, cache, dataSetName, session)
            return frm, 200, {'content-type': 'text/html; charset=utf-8'}

    # Если запрос HTML к не существующей страницы, тогда перебрасываем на  стартовую страницу
    if ext in ["html"]:
        return redirect("/index.html")

    return render_template('404.html; charset=utf-8', **locals()), 404
    # return app.render_template(path)
    # return app.send_static_file(path)


if __name__ == '__main__':
    if os.path.exists(getform.TEMP_DIR_PATH):
        for root, dirs, files in os.walk(getform.TEMP_DIR_PATH):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
    else:
        os.mkdir(getform.TEMP_DIR_PATH)
    port = int(os.environ.get("PORT", 5000))
    if len(sys.argv)>1:
        port = int(sys.argv[1])
    app.run(debug=False, host='0.0.0.0', port=port)