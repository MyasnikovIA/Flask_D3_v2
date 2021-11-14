import os
import shelve

from flask import Flask, redirect, session, render_template
from flask import request, jsonify
from Etc.conf import ConfigOptions, existTempPage, getTempPage, GLOBAL_DICT, nameElementHeshMap

import shutil
import json
from pathlib import Path
import uuid
import getform
import hashlib
from inspect import getfullargspec

from System.d3main import show as d3main_js
from System.d3theme import show as d3theme_css

# https://habr.com/ru/post/222983/
# https://programtalk.com/python-examples/sys.__stdout__/
# https://www.py4u.net/discuss/183138
# https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html

app = Flask(__name__, static_folder='.')
app.secret_key = str(uuid.uuid1()).replace("-", "")
app.config['CORS_HEADERS'] = 'Content-Type'



def sendCostumBin(pathFile):
    # костыль для docker
    txt = ""
    if existTempPage(pathFile):
        txt, mime = getTempPage(pathFile, '')
    if txt == "":
        if os.path.isfile(pathFile):
            with open(pathFile, "rb") as f:
                return f.read(),getform.mimeType(pathFile)
        else:
            return f"File {pathFile} not found {os.path.dirname(Path(__file__))}{os.sep}", getform.mimeType(".txt")
    else:
        return txt, mime


@app.after_request
def after_request(response):
    # CORS in flask
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    header['Server'] = 'D3apiServer'
    return response

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html', **locals()), 404

@app.route('/')
def example():
    # user_agent = request.headers.get('User-Agent')
    # return app.send_static_file('index.html')
    return redirect("/index.html")


@app.route('/~<name>', methods=['GET'])
def d3theme_files(name):
    if "d3theme" in name:
        return d3theme_css(request), 200, {'content-type': 'text/css'}
    if "d3main" in name:
        return d3main_js(request), 200, {'content-type': 'application/x-javascript'}
    return f"/* библиотека не найдена /~{name} */", 200, {'content-type': 'application/x-javascript'}


def getParam(name, defoultValue=''):
    return request.args.get(name, default=defoultValue)

@app.route('/<the_path>.php', methods=['GET', 'POST'])
def getform_php_files(the_path):
    if the_path == 'getform':
        formName = getParam('Form')
        cache = getParam('cache')
        dataSetName = getParam('DataSet', "")
        frm = getform.getParsedForm(formName, cache, dataSetName, session)
        return frm, 200, {'content-type': 'application/plain'}

    if the_path == "request":
        resultTxt = "{}"
        formName = getParam('Form')
        cache = getParam('cache')
        if request.method == 'POST':
            dataSet = json.loads(request.form.get('request'))
            for dataSetName in dataSet:
                typeQuery = dataSet[dataSetName]["type"]
                paramsQuery = dataSet[dataSetName]["params"]
                resultTxt = getform.dataSetQuery(f'{formName}:{dataSetName}', typeQuery, paramsQuery, session)
                # getRunAction(formName, cache, name, queryActionObject[name])
        return resultTxt, 200, {'Content-Type': 'text/xml; charset=utf-8'}

    if the_path == "runScript":
        scrArg = request.form.to_dict(flat=False)
        funName = str(scrArg['WEVENT'])[2:-2]
        args = json.loads(str(scrArg['ARGS'])[2:-2])
        if funName in nameElementHeshMap:
            return getform.runFormScript(nameElementHeshMap[funName], args, session), 200, {
                'content-type': 'application/json'}
        else:
            return f"""{{"error":"код с именем  '{funName}' не определено"}}""", 200, {
                'content-type': 'application/json'}
    """ 
    if the_path == "upload":
        username = request.cookies.get('username')
        f = request.files['the_file']
        f.save('uploads' + secure_filename(f.filename))
    """
    return f"""{{"error":"поведение для команды '{the_path}' не определено в app.py"}}""", 200, {
        'content-type': 'application/json'}

@app.route('/<name>.js')
def js_files(name):
    return app.send_static_file('js/' + name + '.js')


@app.route('/<path:path>')
def all_files(path):
    try:
        # Инициализация информации об агенте()
        if path[-3:].lower() in ["tml", "css", ".js"]:
            getform.getAgentInfo(request)
    except:
        pass
    ROOT_DIR = f"{os.path.dirname(Path(__file__))}{os.sep}"
    # {os.sep})}
    if '/~Cmp' in path and 'Components/' in path:
        cmp = path[path.find('Components/') + len('Components/'): path.find('/~Cmp') - len('/~Cmp') + 1]
        img = path[path.rfind("/"):]
        pathImg = f"{ROOT_DIR}Components/{cmp}/images/default{img}.png"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if path == "index.html" or path == "index.html/":
        pathImg = f"{ROOT_DIR}index.html"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if 'favicon.ico' in path:
        pathImg = f"{ROOT_DIR}{path}"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}

    if 'Components/' in path:
        pathImg = f"{ROOT_DIR}{path}"
        bin, mime = sendCostumBin(pathImg)
        return bin, 200, {'content-type': mime}
    print(path)
    return app.send_static_file(path)


if __name__ == '__main__':
    if "debug" in ConfigOptions and not int(ConfigOptions["debug"]) == 0:
        TEMP_DIR_PATH = os.path.join(os.path.dirname(Path(__file__)), ConfigOptions['TempDir'])
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
