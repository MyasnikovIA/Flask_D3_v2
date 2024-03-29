import os
import codecs
from app import session
from pathlib import Path
import getform

import hashlib

compList = ['Label','Form','Edit','Button' ,'Base','Window','ComboBox','CheckBox','Mask','Dependences','HyperLink','Expander',
            'TextArea','PopupMenu','PopupItem','AutoPopupMenu','ColorEdit','PopupMenu','PopupItem','Dialog','Image','Toolbar','PageControl','Tabs',
            'OpenStreetMap',"OpenStreetMapLabel",'Tree']

def readCmpCss(name, ext=''):
    # ROOT_DIR = session["AgentInfo"]['ROOT_DIR']
    cmpDirSrc = f'{getform.COMPONENT_PATH}{os.sep}{name}{os.sep}css{os.sep}{name}.css'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""

def readfile(name):
    # request.user_agent.platform
    ROOT_DIR = f"{Path(__file__).absolute().parent.parent}{os.sep}"
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{name}'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""


def getSrc(request):
    # request.user_agent.platform
    res = []
    for cmp in compList:
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}css{os.sep}{cmp}.css'
        res.append(readfile(cmpDirSrc))
    # Обязательные стили
    res.append(readfile('Components/Window/css/win.css'))
    res.append(readfile('Components/Layout/css/Layout.css'))
    return "".join(res)


def getTemp(request):
    cmpDirSrc = getform.TEMP_DIR_PATH
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{request.user_agent.platform}_d3theme.css"
    txt = ""
    if getform.existTempPage(cmpFiletmp):
       txt,mime = getform.getTempPage(cmpFiletmp,'')
    if txt == "":
        txt = getSrc(request)
        getform.setTempPage(cmpFiletmp, txt)
        return txt
    else:
        return txt

def getTempOld(request):
    cmpDirSrc = getform.TEMP_DIR_PATH
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{request.user_agent.platform}_d3theme.css"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if getform.existTempPage(cmpFiletmp):
       txt,mime = getform.getTempPage(cmpFiletmp,'')
    if txt == "":
        if not os.path.exists(cmpFiletmp):
            with open(cmpFiletmp,"wb") as d3_css:
                txt = getSrc(request)
                d3_css.write(txt.encode())
                getform.setTempPage(cmpFiletmp,txt)
                return txt
        else:
            with open(cmpFiletmp, "rb") as infile:
                txt = infile.read()
                getform.setTempPage(cmpFiletmp, txt)
                return txt
    else:
        return txt
def show(request):
    # request.user_agent.platform
    return getTemp(request)
