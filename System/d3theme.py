import os
import codecs
from Etc.conf import get_option, ROOT_DIR
import hashlib

theme = get_option('Theme');
compList = ['Label','Form','Edit','Button' ,'Base','Window']

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


def getSrc():
    res = []
    for cmp in compList:
        res.append(readCmpCss(cmp, ''))
        res.append(readfile('Components/Window/css/win.css'))
        res.append(readfile('Components/Layout/css/Layout.css'))
    return "\r".join(res)


def getTemp():
    cmpDirSrc = f'{ROOT_DIR}{os.sep}{get_option("TempDir","temp/")}'
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    if not os.path.exists(f"{cmpDirSrc}d3theme.css"):
        d3_js = open(f"{cmpDirSrc}d3theme.css", 'w')
        txt = getSrc()
        d3_js.write(txt)
        d3_js.close()
        return txt
    else:
        with open(f"{cmpDirSrc}d3theme.css", "rb") as infile:
            return infile.read()

def show():
    if get_option("TempDir") and (+get_option("debug"))<1:
        return getTemp()
    else:
        return getSrc()
