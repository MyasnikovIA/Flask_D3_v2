import os

from flask import Flask,redirect, session
from flask import request, jsonify
from Etc.conf import ConfigOptions,existTempPage,getTempPage


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


# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================

def mimeType(pathFile):
    extList = {"py": "text/html", "psp": "text/html", "css": "text/css", "js": "application/x-javascript",
               "xml": "text/xml", "dtd": "text/xml", "txt": "text/plain", "inf": "text/plain",
               "nfo": "text/plain",
               "php": "text/plain", "html": "text/html", "csp": "text/html", "htm": "text/html",
               "shtml": "text/html",
               "shtm": "text/html", "stm": "text/html", "sht": "text/html", "sht": "text/html",
               "csp": "text/html",
               "mac": "text/html", "cls": "text/html", "jpg": "image/jpeg", "cos": "text/html",
               "mpeg": "video/mpeg",
               "mpg": "video/mpeg", "mpe": "video/mpeg", "ai": "application/postscript", "zip": "application/zip",
               "zsh": "text/x-script.zsh", "x-png": "image/png", "xls": "application/x-excel",
               "xlm": "application/excel",
               "wav": "audio/x-wav", "txt": "text/plain", "tiff": "image/tiff", "tif": "image/x-tiff",
               "text": "text/plain",
               "swf": "application/x-shockwave-flash", "sprite": "application/x-sprite",
               "smil": "application/smil",
               "sh": "text/x-script.sh", "rtx": "text/richtext", "rtf": "text/richtext",
               "pyc": "application/x-bytecode.python",
               "png": "image/png", "pic": "image/pict", "mp3": "video/mpeg", "mp2": "video/mpeg",
               "movie": "video/x-sgi-movie",
               "mov": "video/quicktime", "mjpg": "video/x-motion-jpeg", "mime": "www/mime",
               "mif": "application/x-mif",
               "midi": "audio/midi", "js": "application/javascript", "jpeg": "image/jpeg", "jps": "image/x-jps",
               "jam": "audio/x-jam",
               "jav": "text/plain", "java": "text/x-java-source", "htm": "text/html", "html": "text/html",
               "gzip": "application/x-gzip", "gif": "image/gif", "gl": "video/gl", "csh": "text/x-script.csh",
               "css": "text/css", "bsh": "application/x-bsh", "bz": "application/x-bzip",
               "bz2": "application/x-bzip2",
               "c": "text/plain", "c++": "text/plain", "cat": "application/vnd.ms-pki.seccat", "cc": "text/plain",
               "htmls": "text/html", "bmp": "image/bmp", "bm": "image/bmp", "avi": "video/avi",
               "avs": "video/avs-video",
               "au": "audio/basic", "arj": "application/arj", "art": "image/x-jg", "asf": "video/x-ms-asf",
               "asm": "text/x-asm",
               "asp": "text/asp"}


# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================
def getSession(name, defoult):
    if not name in session:
        return defoult
    return session[name]

def setSession(name, value):
    session[name] = value


def getSessionObject():
    return session

def getAgentInfo(request):
    if not "AgentInfo" in session:
        session["AgentInfo"]={}
    if not request.user_agent is None:
        session["AgentInfo"]={}
        session["AgentInfo"]['User-Agent'] = request.headers.get('User-Agent')
        session["AgentInfo"]['browser'] = request.user_agent.browser
        session["AgentInfo"]['version'] = request.user_agent.version and int(request.user_agent.version.split('.')[0])
        session["AgentInfo"]['platform'] = request.user_agent.platform
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            session["AgentInfo"]['ip'] = request.environ['REMOTE_ADDR']
        else:
            session["AgentInfo"]['ip'] = request.environ['HTTP_X_FORWARDED_FOR']
    session["AgentInfo"]['Forms'] = ConfigOptions['Forms']
    if not 'debug' in session["AgentInfo"] and request.args.get("debug") == None:
        session["AgentInfo"]['debug'] = ConfigOptions['debug']
    if not request.args.get("debug") == None:
        session["AgentInfo"]['debug'] = request.args.get("debug")
    if not 'UserForms' in session["AgentInfo"] and request.args.get("f") == None:
        session["AgentInfo"]['UserForms'] = ConfigOptions['UserForms']
    if not request.args.get("f") == None:
        session["AgentInfo"]['UserForms'] = request.args.get("f")
    session["AgentInfo"]['TempDir'] = ConfigOptions['TempDir']
    session["AgentInfo"]['ROOT_DIR'] = f"{os.path.dirname(Path(__file__))}{os.sep}"
    session["AgentInfo"]['TEMP_DIR_PATH'] = os.path.join(os.path.dirname(Path(__file__)),ConfigOptions['TempDir'])
    return session["AgentInfo"]
# ====================================================================================================================
# ====================================================================================================================

def sendCostumBin(pathFile):
    txt = ""
    if existTempPage(pathFile):
        txt, mime = getTempPage(pathFile, '')
    if txt == "":
        if os.path.isfile(pathFile):
            with open(pathFile, "rb") as f:
                return f.read(), mimeType(pathFile)
        else:
            return f"File {pathFile} not found", mimeType(".txt")
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

@app.route('/')
def example():
    #user_agent = request.headers.get('User-Agent')
    #return app.send_static_file('index.html')
    return redirect("/index.html")


@app.route('/~<name>', methods=['GET'])
def d3theme_files(name):
    if "d3theme" in name:
        # return app.send_static_file('external/d3/d3theme.css')
        # return app.send_static_file('external/d3/~d3theme'), 200, {'content-type': 'text/css'}
        return d3theme_css(session), 200, {'content-type': 'text/css'}

    if "d3main" in name:
        # return app.send_static_file('external/d3/d3api.js')
        # return app.send_static_file('System/d3main.py'), 200, {'content-type': 'application/json'}
        return d3main_js(session), 200, {'content-type': 'application/json'}

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


    if the_path == "upload":
        username = request.cookies.get('username')
        f = request.files['the_file']
        f.save('uploads' + secure_filename(f.filename))

    return f"""{{"error":"поведение для команды '{the_path}' не определено в app.py"}}""", 200, {'content-type': 'application/json'}


@app.route('/<name>.js')
def js_files(name):
    return app.send_static_file('js/' + name + '.js')


@app.route('/<path:path>')
def all_files(path):
    if path[-3:].lower() in ["tml","css",".js"]:
        getAgentInfo(request)
    ROOT_DIR = session["AgentInfo"]['ROOT_DIR']
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
    if "debug" in ConfigOptions and not ConfigOptions["debug"] == '0':
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
    app.run(debug=True, host='0.0.0.0', port=port)
