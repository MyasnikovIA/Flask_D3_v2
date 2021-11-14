import json
from flask import session, request, jsonify
import os
import codecs
import hashlib
import getform
from app import session

compList = ['Base','Edit','Button','Form','Label','LayoutSplit','ComboBox','CheckBox','Mask','Dependences','HyperLink','Expander',
            'TextArea','PopupMenu','PopupItem','AutoPopupMenu','ColorEdit','PopupMenu','PopupItem','Dialog','Image','Toolbar','PageControl','Tabs',
            'OpenStreetMap',"OpenStreetMapLabel",'Tree','Server']

def readfile(name):
    ROOT_DIR = session["AgentInfo"]['ROOT_DIR']
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{name}'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""

def getIdClient():
    agent = request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR'], "agent": agent})
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR'], "agent": agent})


def genCacheUid():
    random = "c"
    hesh = random + hashlib.md5(f'{getIdClient()}'.encode('utf-8')).hexdigest()
    return hesh

def getTemp(request):
    ROOT_DIR = session["AgentInfo"]['ROOT_DIR']
    cmpDirSrc = session["AgentInfo"]['TEMP_DIR_PATH']
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{request.user_agent.platform}_d3main.js"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if getform.existTempPage(cmpFiletmp):
        txt,mime  = getform.getTempPage(cmpFiletmp,'')
    if not txt == "":
        return txt
    if not os.path.exists(cmpFiletmp):
        with open(cmpFiletmp,"wb") as d3_js:
            txt = getSrc(request)
            d3_js.write(txt.encode())
            getform.setTempPage(cmpFiletmp, txt)
            return txt
    else:
        with open(cmpFiletmp, "rb") as infile:
            txt = infile.read()
            getform.setTempPage(cmpFiletmp, txt)
            return txt


def getSrc(request):
    random = "c"
    hesh = random + hashlib.md5(f'{getIdClient()}'.encode('utf-8')).hexdigest()
    res = []
    res.append('(function(){')
    res.append(readfile('System/js/polyfill.js'))
    res.append(readfile('System/js/clipboard.min.js'))

    # Добавляем в фрэймворк информацию о платформе
    if "AgentInfo" in session:
        res.append(f'\r var AGENT_INFO_PLATFORM = "{request.user_agent.platform}";')
    # ============================================

    # Добавил функцию отладки (для Android)
    res.append("""
    /* Функция отладки ghbvty*/
    var console_log = function(message){
       if ((AGENT_INFO_PLATFORM == "android") && (Android)) {
         msg="";
         for (let args of arguments) {
            if (typeof args === 'string') {
               msg+="|"+args;
            }
            if (typeof args === 'object') {
               try {
                 msg+="|"+JSON.stringify(args);
               } catch {
                 msg+="|"+args;
               }
            }
         }
         Android.console_log(msg);
       } else {
         console.log(arguments);
       }
    }
    var log = console_log; 
    """)


    res.append(readfile('System/js/main.js'))
    res.append(readfile('System/js/dataset.js'))
    res.append(readfile('System/js/action.js'))
    res.append(readfile('System/js/module.js'))
    res.append(readfile('System/js/repeater.js'))
    res.append(readfile('System/js/common.js'))
    res.append(readfile('System/js/md5.js'))
    res.append(readfile('System/js/notify.js'))
    res.append(readfile('System/js/crc32/crc32.js'))
    # подключаем компоненты
    res.append(readfile('System/js/Base.js'))
    res.append(readfile('Components/Window/common.js'))
    res.append(readfile('Components/Window/win_sys.js'))
    res.append(readfile('Components/Window/window.js'))

    # подключаем библиотеку OSM
    # res.append(readfile(session,'Components/OpenStreetMap/js/OpenLayers.js'))

    #res.append(readfile('Components/Layout/js/Layout.js'))
    #res.append(readfile('Components/LayoutSplit/js/LayoutSplit.js'))
    for cmp in compList:
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}js{os.sep}{cmp}.js'
        res.append(readfile(cmpDirSrc))

    res.append('})();\r')
    res.append(f'\rD3Api.SYS_CACHE_UID = "{genCacheUid()}";')
    res.append('\rD3Api.SYS_CONFIG = {"formCache":false,"showDependence":false};')
    res.append('\rD3Api.SYS_CONFIG.debug = 1;')
    res.append('\rD3Api.startInit = function (){};')
    # res.append(f'\rD3Api.agent_info = { json.dumps(agent_info)};')
    return "".join(res)


def show(request):
    if "AgentInfo" in session and "TempDir" in session["AgentInfo"] and 'debug' in session["AgentInfo"] and int(session["AgentInfo"]['debug']) == 0:
        return getTemp(request)
    return getSrc(request)

    #if get_option("TempDir") and (+get_option("debug"))<1:
    #    return getTemp(agent_info)
    #else:
    #    return getSrc(agent_info)

