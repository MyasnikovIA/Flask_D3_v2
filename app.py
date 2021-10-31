import os

from flask import Flask,redirect, session
from flask import request, jsonify
from getform import *
import shutil
import json
import copy
import hashlib
from inspect import getfullargspec

from Etc.conf import get_option, ROOT_DIR
from System.d3main import show as d3main_js
from System.d3theme import show as d3theme_css

# https://habr.com/ru/post/222983/
# https://programtalk.com/python-examples/sys.__stdout__/
# https://www.py4u.net/discuss/183138

app = Flask(__name__, static_folder='.')
app.secret_key = str(uuid.uuid1()).replace("-", "")
app.config['CORS_HEADERS'] = 'Content-Type'
TEMP_DIR_PATH = f'{ROOT_DIR}{os.sep}{get_option("TempDir", "temp/")}'


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

"""
global SESSION
SESSION = {}

def getSession(name, defoult):
    global SESSION
    key = getIdClient()
    if not key in SESSION:
        SESSION[key] = {}
        return defoult
    if not name in SESSION[key]:
        return defoult
    return SESSION[key][name]


def setSession(name, value):
    global SESSION
    key = getIdClient()
    if not key in SESSION:
        SESSION[key] = {}
    SESSION[key][name] = value


def getSessionObject():
    global SESSION
    key = getIdClient()
    if not key in SESSION:
        SESSION[key] = {}
    return SESSION[key]


def getIdClient():
    agent = request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR'], "agent": agent})
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR'], "agent": agent})

"""
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
def getAgentObj(req):
    user_agent = request.headers.get('User-Agent')
    browser = request.user_agent.browser
    version = request.user_agent.version and int(req.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    #uas = request.user_agent.string
    return {'user_agent':user_agent,'browser':browser,'version':version,'platform':platform}
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
    user_agent = request.headers.get('User-Agent')
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    agent_info = {'user_agent':user_agent,'browser':browser,'version':version,'platform':platform}

    if "d3theme" in name:
        # return app.send_static_file('external/d3/d3theme.css')
        return d3theme_css(agent_info), 200, {'content-type': 'text/css'}
        # return app.send_static_file('external/d3/~d3theme'), 200, {'content-type': 'text/css'}

    if "d3main" in name:
        # return app.send_static_file('external/d3/d3api.js')
        return d3main_js(agent_info), 200, {'content-type': 'application/json'}
        # return app.send_static_file('System/d3main.py'), 200, {'content-type': 'application/json'}


@app.route('/<the_path>.php', methods=['GET', 'POST'])
def getform_php_files(the_path):
    user_agent = request.headers.get('User-Agent')
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    agent_info = {'user_agent':user_agent,'browser':browser,'version':version,'platform':platform}
    if the_path == 'getform':
        formName = getParam('Form')
        cache = getParam('cache')
        dataSetName = getParam('DataSet', "")
        frm = getParsedForm(formName, cache, dataSetName, agent_info)
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
                resultTxt = dataSetQuery(f'{formName}:{dataSetName}', typeQuery, paramsQuery, session, agent_info)
                # getRunAction(formName, cache, name, queryActionObject[name])
        return resultTxt, 200, {'Content-Type': 'text/xml; charset=utf-8'}
    return f"""{{"error":"поведение для команды '{the_path}' не определено в app.py"}}""", 200, {
        'content-type': 'application/xml'}


@app.route('/<name>.js')
def js_files(name):
    return app.send_static_file('js/' + name + '.js')


@app.route('/<path:path>')
def all_files(path):
    print(request.args.get("debug"))
    global ConfigOptions
    configOptions = copy.copy(ConfigOptions)
    if not request.args.get("debug") == None:
        configOptions["debug"] = request.args.get("debug")
    if not request.args.get("f") == None:
        configOptions["UserForms"] = request.args.get("f")

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
    if get_option("debug") > 0:
        if os.path.exists(TEMP_DIR_PATH):
            for root, dirs, files in os.walk(TEMP_DIR_PATH):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
        else:
            os.mkdir(TEMP_DIR_PATH)
    app.debug = True
    app.run(host='0.0.0.0', port=9091)
