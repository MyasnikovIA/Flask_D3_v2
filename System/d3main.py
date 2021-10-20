from flask import session, request, jsonify
import os
import codecs
from Etc.conf import get_option, ROOT_DIR, getTempPage, setTempPage, existTempPage
import hashlib

compList = ['Base','Edit','Button','Form','Label','LayoutSplit','ComboBox']

def readfile(name):
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

def getTemp(agent_info):
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{get_option("TempDir","temp/")}'
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{agent_info.get('platform')}_d3main.js"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if existTempPage(cmpFiletmp):
        txt,mime  = getTempPage(cmpFiletmp,'')
    if not txt == "":
        return txt

    if not os.path.exists(cmpFiletmp):
        with open(cmpFiletmp,"wb") as d3_js:
            txt = getSrc(agent_info)
            d3_js.write(txt.encode())
            setTempPage(cmpFiletmp, txt)
            return txt
    else:
        with open(cmpFiletmp, "rb") as infile:
            txt = infile.read()
            setTempPage(cmpFiletmp, txt)
            return txt


def getSrc(agent_info):
    random = "c"
    hesh = random + hashlib.md5(f'{getIdClient()}'.encode('utf-8')).hexdigest()
    res = []
    res.append('(function(){')
    res.append(readfile('System/js/polyfill.js'))
    res.append(readfile('System/js/clipboard.min.js'))
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
    #res.append(readfile('Components/Layout/js/Layout.js'))
    #res.append(readfile('Components/LayoutSplit/js/LayoutSplit.js'))
    for cmp in compList:
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}js{os.sep}{cmp}.js'
        res.append(readfile(cmpDirSrc))
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}js{os.sep}{cmp}_{agent_info.get("platform")}.js'
        res.append(readfile(cmpDirSrc))



    #
    # дописать инициализацию D3 в колбэк
    # res.append("""
    # document.addEventListener('DOMContentLoaded', function() {
    #    var styleSheet = document.createElement("style");
    #    var text = document.createTextNode("* {filter: none !important; } \n.hidden {visibility: hidden;}");
    #    styleSheet.appendChild(text);
    #    document.head.appendChild(styleSheet);
    #
    #    if (document.getElementById('D3MainContainer') == null){
    #        var d3MainContainer = document.createElement('div');
    #        d3MainContainer.id = 'D3MainContainer';
    #        document.body.appendChild(d3MainContainer);
    #    }
    #
    #    if (document.getElementsByClassName('MContent').length == 0){
    #        var _mainContainer = document.createElement('div');
    #        _mainContainer.id = '_mainContainer';
    #        _mainContainer.classList.add('MContent')
    #        document.getElementById('D3MainContainer').appendChild(_mainContainer);
    #    }
    #
    #    // Инициализируем D3
    #    if (typeof(D3Api.MULTI_REQUEST) === 'undefined'){
    #       D3Api.MULTI_REQUEST = {"MAX_THREAD":"","MAX_REQUEST":""};
    #       D3Api.cache_enabled = 0;
    #       D3Api.startInit();
    #       D3Api.init();
    #       D3Api.MainDom = document.getElementById('D3MainContainer');
    #       D3Api.D3MainContainer = D3Api.MainDom;
    #       var dev_info_panel = D3Api.getOption('dev_info_panel', 'false');
    #       if (dev_info_panel && dev_info_panel.show == 'true') {
    #           var info_panel = document.createElement('div');
    #           if (dev_info_panel.text) {
    #               info_panel.innerHTML = dev_info_panel.text;
    #           }
    #           if (dev_info_panel.color) {
    #               info_panel.style.borderColor = dev_info_panel.color;
    #           }
    #           D3Api.addClass(info_panel, 'dev_info_panel');
    #           D3Api.insertBeforeDom(D3Api.D3MainContainer, info_panel);
    #       }
    #    }
    #    if (D3Api.onload) {
    #        D3Api.onload();
    #    }
    #    // D3Api.showForm('main', undefined, {history: false});
    # }, true);
    # """)

    res.append('})();')
    res.append(f'D3Api.SYS_CACHE_UID = "{genCacheUid()}";')
    res.append('D3Api.SYS_CONFIG = {"formCache":false,"showDependence":false};')
    res.append('D3Api.SYS_CONFIG.debug = 1;')
    res.append('D3Api.startInit = function (){};')
    return "".join(res)


def show(agent_info):
    if get_option("TempDir") and (+get_option("debug"))<1:
        return getTemp(agent_info)
    else:
        return getSrc(agent_info)
