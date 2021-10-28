import os
import codecs
from Etc.conf import get_option, ROOT_DIR, getTempPage, setTempPage, existTempPage
import hashlib

theme = get_option('Theme');
compList = ['Label','Form','Edit','Button' ,'Base','Window','ComboBox','CheckBox','Mask','Dependences','HyperLink','Expander',
            'TextArea','PopupMenu','PopupItem','AutoPopupMenu','ColorEdit','PopupMenu','PopupItem']

def readCmpCss(name, ext=''):
    cmpDirSrc = f'{ROOT_DIR}Components{os.sep}{name}{os.sep}css{os.sep}{name}.css'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""


def readfile(name):
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{name}'
    if os.path.exists(cmpDirSrc):
        with codecs.open(cmpDirSrc, encoding='utf-8') as f:
            file_text = f.read()
        return file_text
    return ""


def getSrc(agent_info):
    res = []
    for cmp in compList:
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}css{os.sep}{cmp}.css'
        res.append(readfile(cmpDirSrc))
        cmpDirSrc = f'Components{os.sep}{cmp}{os.sep}css{os.sep}{cmp}_{agent_info.get("platform")}.css'
        res.append(readfile(cmpDirSrc))
    # Обязательные стили
    res.append(readfile('Components/Window/css/win.css'))
    res.append(readfile(f'Components/Window/css/win_{agent_info.get("platform")}.css'))
    res.append(readfile('Components/Layout/css/Layout.css'))
    res.append(readfile(f'Components/Window/css/win_{agent_info.get("platform")}.css'))
    return "".join(res)

def getTemp(agent_info):
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{get_option("TempDir","temp/")}'
    cmpFiletmp = f"{cmpDirSrc}{os.sep}{agent_info.get('platform')}_d3theme.css"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if existTempPage(cmpFiletmp):
       txt,mime = getTempPage(cmpFiletmp,'')
    if txt == "":
        if not os.path.exists(cmpFiletmp):
            with open(cmpFiletmp,"wb") as d3_css:
                txt = getSrc(agent_info)
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

def show(agent_info):
    if get_option("TempDir") and (+get_option("debug"))<1:
        return getTemp(agent_info)
    else:
        return getSrc(agent_info)
