import json
from flask import session, request, jsonify
import os
import codecs
import hashlib
import getform
from pathlib import Path
from app import session
from werkzeug.urls import url_parse

compList = ['Base','Edit','Button','Form','Label','LayoutSplit','ComboBox','CheckBox','Mask','Dependences','HyperLink','Expander',
            'TextArea','PopupMenu','PopupItem','AutoPopupMenu','ColorEdit','PopupMenu','PopupItem','Dialog','Image','Toolbar','PageControl','Tabs',
            'OpenStreetMap',"OpenStreetMapLabel",'Tree']

def readfile(name):
    cmpDirSrc = f'{getform.ROOT_DIR}{os.sep}{name}'
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
    cmpDirSrc = getform.TEMP_DIR_PATH
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
    elif request.user_agent:
        res.append(f'\r var AGENT_INFO_PLATFORM = "{request.user_agent.platform}";')
    # ============================================

    # Добавил функцию отладки (для Android)
    res.append(""" """)


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
    # res.append(readfile('Components/Layout/js/Layout.js'))
    # res.append(readfile('Components/LayoutSplit/js/LayoutSplit.js'))
    for cmp in compList:
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}js{os.sep}{cmp}.js'
        res.append(readfile(cmpDirSrc))

    res.append('})();\r')
    res.append(f'\rD3Api.SYS_CACHE_UID = "{genCacheUid()}";')
    res.append('\rD3Api.SYS_CONFIG = {"formCache":false,"showDependence":false};')
    res.append('\rD3Api.SYS_CONFIG.debug = 1;')
    res.append('\rD3Api.startInit = function (){};\r')
    #--------------------------------------
    res.append(f"""
 D3Api.MULTI_REQUEST = {{"MAX_THREAD":"","MAX_REQUEST":""}};
 D3Api.cache_enabled = 0;
 D3Api.startInit();
 D3Api.init();
 // D3Api.showForm('Tutorial/main', undefined, {{history: false}});
 window.addEventListener('DOMContentLoaded', function() {{
      D3Api.MainDom = document.body;
      D3Api.D3MainContainer = D3Api.MainDom;
      document.oncontextmenu="return D3Api.onContextMenuBody(event);";
      var formText = D3Api.MainDom.outerHTML.replace("</body"+">", "")
           .replace('<div cmptype=\"sysinfo\" style=\"display:none;\">', '</div><div cmptype=\"sysinfo\" style=\"display:none;\">')
           .replace("<body ", "<div cmptype='Form' ");
      D3Api.MainDom.innerHTML = '';
      D3Api.MainDom.removeAttribute("name");
      D3Api.MainDom.removeAttribute("class");
      D3Api.MainDom.setAttribute("id","D3MainContainer");
      data = {{}};                                 // дописать инициализацию переменных
      form = new D3Api.D3Form("{url_parse(request.referrer).path[1:]}", formText); // дописать инициализацию имени открываемой формы 
      form.show(data, D3Api.MainDom);
      D3Api.MainDom = D3Api.MainDom.firstChild;
      D3Api.D3MainContainer = D3Api.MainDom;
      D3Api.isFrameWindow = false; // окно открыто внутри IFRAME
      if (window.frames.frameElement) {{
         D3Api.isFrameWindow = true;
      }}
      // Получение переменных из родительского окна
      var dataItemsName = "D3(tmp):/{url_parse(request.referrer).path[1:]}:history_state";
      if (localStorage.getItem(dataItemsName)) {{
         var formObj = JSON.parse(localStorage.getItem(dataItemsName));
         localStorage.removeItem(dataItemsName);
         if ( (formObj['data']) && (formObj['data']['vars']) ) {{
            for (var key in formObj["data"]['vars']) {{
               D3Api.setVar(key, formObj["data"]['vars'][key]);
            }}
         }}
      }}
 }},true);
    """)

    cmpDirSrc = f'System{os.sep}js{os.sep}mobile_touchpad_event_processing.js'
    res.append(readfile(cmpDirSrc))
    # res.append(f'\rD3Api.agent_info = { json.dumps(agent_info)};')
    return "".join(res)


def show(request):
    return getTemp(request)

