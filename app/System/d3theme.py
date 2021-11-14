import os
import codecs
from Etc.conf import getTempPage, setTempPage, existTempPage
from app import session
from pathlib import Path

import hashlib

compList = ['Label','Form','Edit','Button' ,'Base','Window','ComboBox','CheckBox','Mask','Dependences','HyperLink','Expander',
            'TextArea','PopupMenu','PopupItem','AutoPopupMenu','ColorEdit','PopupMenu','PopupItem','Dialog','Image','Toolbar','PageControl','Tabs',
            'OpenStreetMap',"OpenStreetMapLabel",'Tree','Server']

def readCmpCss(name, ext=''):
    ROOT_DIR = session["AgentInfo"]['ROOT_DIR']
    cmpDirSrc = f'{ROOT_DIR}Components{os.sep}{name}{os.sep}css{os.sep}{name}.css'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""

def readfile(name):
    # request.user_agent.platform
    ROOT_DIR = f"{Path(__file__).parent.parent}{os.sep}"
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
    cmpDirSrc = session["AgentInfo"]['TEMP_DIR_PATH']
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{request.user_agent.platform}_d3theme.css"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if existTempPage(cmpFiletmp):
       txt,mime = getTempPage(cmpFiletmp,'')
    if txt == "":
        if not os.path.exists(cmpFiletmp):
            with open(cmpFiletmp,"wb") as d3_css:
                txt = getSrc(request)
                d3_css.write(txt.encode())
                setTempPage(cmpFiletmp,txt)
                return txt
        else:
            with open(cmpFiletmp, "rb") as infile:
                txt = infile.read()
                setTempPage(cmpFiletmp, txt)
                return txt
    else:
        return txt

def show(request):
    # request.user_agent.platform
    if "AgentInfo" in session and "TempDir" in session["AgentInfo"] and 'debug' in session["AgentInfo"] and session["AgentInfo"]['debug'] == "0":
        return getTemp(request)
    return getSrc(request)
