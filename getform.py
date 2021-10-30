import codecs
import importlib
import os.path
import uuid
import ast
import json
import sys
import re

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from xml.dom import minidom

from app import getSession, setSession
from Etc.conf import *

global COMPONENT_PATH
COMPONENT_PATH = os.path.join(os.path.dirname(__file__), 'Components')
FORM_PATH = os.path.join(os.path.dirname(__file__), get_option('Forms', '/Forms/')[1:])
USER_FORM_PATH = os.path.join(os.path.dirname(__file__), get_option('UserForms', '/UserForms/')[1:])
TEMP_DIR_PATH = os.path.join(os.path.dirname(__file__), get_option('cache_dir'))


def stripCode(srcCode=""):
    """
    Функция очистки пробелов до первого символа (на  пробела), и выравневания остальных строк по этот символ
    :param srcCode:
    :return:
    """
    codeLines = srcCode.split("\n")
    countlines = 0
    startPosition = 0
    codeRes = []
    for line in codeLines:
        oneText = line.lstrip()
        if countlines == 0 and len(oneText) == 0:
            continue
        if countlines == 0 and len(oneText) != 0:
            startPosition = line.find(oneText),
        countlines += 1
        codeRes.append(line[startPosition[0]:])
    codeRes.append("locals()")
    code = '\n'.join(codeRes)
    return code


def exec_then_eval(vars, code, sessionObj):
    """
    Запуск многострочного текста кода  с кэшированием
    :param vars:  переменные для входных рагументов скрипта (инициализация) {"var1":111,"var2":333}
    :param code: текст программы Python для выполнения
    :return:
    """
    block = ast.parse(code, mode='exec')
    # assumes last node is an expression
    last = ast.Expression(block.body.pop().value)
    for ind in globals():
        if not ind[0:2] == '__' and not str(type(globals()[ind])) == "<class 'function'>" \
                and not str(type(globals()[ind])) == "<class 'module'>" \
                and not str(type(globals()[ind])) == "<class 'type'>" \
                and not ind == "request":
            vars[ind] = globals()[ind]
    vars["session"] = sessionObj
    vars["getSession"] = getSession
    vars["setSession"] = setSession
    _globals, _locals = vars, {}
    exec(compile(block, '<string>', mode='exec'), _globals, _locals)
    return eval(compile(last, '<string>', mode='eval'), _globals, _locals)


def getObjctClass(module_class_string, **kwargs):
    """
     Получить экземпляр класса по его полному имени, и инициализироватьобъект с входящими переменными
     Пример:
        defName = os.path.join('Components', "Base", f'BaseCtrl.Base').replace(os.sep, ".")
        obj = getObjctClass(defName, attrs=attrib)
    """
    module_name, class_name = module_class_string.rsplit(".", 1)
    module = importlib.import_module(module_name)
    assert hasattr(module, class_name), "class {} is not in {}".format(class_name, module_name)
    cls = getattr(module, class_name)
    obj = cls(**kwargs)
    # if hasattr(obj, 'Show'):
    #    obj.Show()
    # if hasattr(obj, 'tagName'):
    #     print(f"</{obj.tagName}>", end="")
    return obj


def parseFrm(root, formName, parentRoot={}, num_element=0, agent_info={}):
    """
    Функция предназначена для рекурсивного обхода дерева XML (формы),
    и заены  элементов тэк который начинается с стмволов "cmp" (<cmpButton name="test">)
    Фрагменты для замены описываются в директории Components/<name>/<name>Ctrl.py

    Components/<name1>/<name1>Ctrl.<name2>
    <name1> - имя компонента , без первых букв "cmp"  (<cmpButton/> Имя копонента будет "Button")
    <name2> - название кдласса, который расположен в файле "Components/<name>/<name>Ctrl.py"

    """
    attrib = root.attrib.copy()
    htmlContent = []
    if len(root.attrib) > 0:
        data = " ".join(f' {k}="{v}"' for k, v in root.attrib.items())
    else:
        data = ""

    sysinfoBlock = []
    if 'cmptype' in root.keys():
        compName = root.attrib['cmptype']
    else:
        compName = root.tag
        if compName[:3] == 'cmp':
            compName = compName[3:]
    attrib["tagName"] = compName
    attrib["tag"] = root.tag
    if not root.tail == None:
        attrib["tail"] = root.tail
    if not root.text == None:
        attrib["text"] = root.text
    attrib["formName"] = formName
    attrib["parentElement"] = parentRoot
    attrib["nodeXML"] = root
    attrib["num_element"] = num_element
    attrib["agent_info"] = agent_info
    # дописать проверку наличия компонента файла
    compFileName = os.path.join(COMPONENT_PATH, compName, f'{compName}Ctrl.py')
    if os.path.isfile(compFileName):
        is_enyTag = 1
        defName = os.path.join('Components', compName, f'{compName}Ctrl.{compName}').replace(os.sep, ".")
        if not "name" in attrib:
            attrib["name"] = str(uuid.uuid1()).replace("-", "")
    else:
        is_enyTag = 0
        defName = os.path.join('Components', "Html", f'HtmlCtrl.Html').replace(os.sep, ".")
    obj = getObjctClass(defName, attrs=attrib)
    if not root.text == None and root.tail == None:
        if is_enyTag == 0:
            htmlContent.append(f"<{root.tag}{data}>")
            htmlContent.append(root.text)
        else:
            # print(obj.text, end="")
            obj.show()
            if hasattr(obj, 'SetSysInfo'):
                sysinfoBlock.extend(obj.SetSysInfo)
            if hasattr(obj, 'HTML_DST'):
                htmlContent.append("".join(obj.HTML_DST))


    elif root.text == None and not root.tail == None:
        if is_enyTag == 0:
            # если тэг закрытый
            htmlContent.append(f"<{root.tag}{data}/>")
        else:
            # print(f"<{obj.tag}{data}/>", end="")
            obj.show()
            if hasattr(obj, 'HTML_DST'):
                htmlContent.append("".join(obj.HTML_DST))
            if hasattr(obj, 'SetSysInfo'):
                sysinfoBlock.extend(obj.SetSysInfo)

    elif not root.text == None and not root.tail == None:
        if is_enyTag == 0:
            htmlContent.append(f"<{root.tag}{data}>")
            htmlContent.append(root.text)
        else:
            # print(f"<{obj.tag}{data}>", end="")
            # print(obj.text, end="")
            obj.show()
            if hasattr(obj, 'HTML_DST'):
                htmlContent.append("".join(obj.HTML_DST))
            if hasattr(obj, 'SetSysInfo'):
                sysinfoBlock.extend(obj.SetSysInfo)
            if hasattr(obj, 'text') and not obj.text == None:
                htmlContent.append(obj.text)
    # =========== Рекурсионый обход дерева ============================
    if hasattr(root, 'getchildren'):
        for elem in root.getchildren():
            loc_SetSysInfo, text = parseFrm(elem, formName, root, 0)
            sysinfoBlock.extend(loc_SetSysInfo)
            htmlContent.append(text)
    elif len(root) > 0:
        num_element = 0
        for elem in root:
            num_element += 1
            loc_SetSysInfo, text = parseFrm(elem, formName, root, num_element)
            sysinfoBlock.extend(loc_SetSysInfo)
            htmlContent.append(text)
    # =================================================================

    if not root.text == None and root.tail == None:
        if is_enyTag == 0:
            htmlContent.append(f"</{root.tag}>")
        else:
            if len(obj.tag) > 0 and not hasattr(obj, 'tagCls'):
                htmlContent.append(f"</{obj.tag}>")
            elif hasattr(obj, 'tagCls'):
                htmlContent.append(obj.tagCls)
            elif hasattr(obj, 'SysInfoTag') and len(obj.SysInfoTag) > 0:
                sysinfoBlock.append(f"</{obj.SysInfoTag}>")

    elif root.text == None and not root.tail == None:
        if is_enyTag == 0:
            htmlContent.append(root.tail)
        else:
            if len(obj.tag) > 0 and not hasattr(obj, 'tagCls'):
                htmlContent.append(f"</{obj.tag}>")
            elif hasattr(obj, 'tagCls'):
                htmlContent.append(obj.tagCls)
            elif hasattr(obj, 'SysInfoTag') and len(obj.SysInfoTag) > 0:
                sysinfoBlock.append(f"</{obj.SysInfoTag}>")
            htmlContent.append(obj.tail)
    elif not root.text == None and not root.tail == None:
        if is_enyTag == 0:
            if hasattr(obj, 'tag'):
                if len(obj.tag) > 0 and not hasattr(obj, 'tagCls'):
                    htmlContent.append(f"</{obj.tag}>")
                elif hasattr(obj, 'tagCls'):
                    htmlContent.append(obj.tagCls)
                elif hasattr(obj, 'SysInfoTag') and len(obj.SysInfoTag) > 0:
                    sysinfoBlock.append(f"</{obj.SysInfoTag}>")
            else:
                htmlContent.append(f"</{root.tag}>")
            htmlContent.append(root.tail)
        else:
            if len(obj.tag) > 0 and not hasattr(obj, 'tagCls'):
                htmlContent.append(f"</{obj.tag}>")
            elif hasattr(obj, 'tagCls'):
                htmlContent.append(obj.tagCls)
            elif hasattr(obj, 'SysInfoTag') and len(obj.SysInfoTag) > 0:
                sysinfoBlock.append(f"</{obj.SysInfoTag}>")
            htmlContent.append(obj.tail)
    return sysinfoBlock, "".join(htmlContent)


def getSrc(formName, cache, dataSetName="", agent_info={}):
    # cmpFiletmp = f"{cmpDirSrc}{os.sep}{agent_info['platform']}_{formName.replace(os.sep, '_')}{blockName}.frm"
    rootForm = getXMLObject(formName)
    sysinfoBlock, text = parseFrm(rootForm, formName,{},0,agent_info)  # парсим форму
    resTxt = [text]
    resTxt.append('\n<div cmptype="sysinfo" style="display:none;">')
    for line in sysinfoBlock:
        resTxt.append(line)
    resTxt.append('</div>')
    return "".join(resTxt)


def getTemp(formName, cache, dataSetName, agent_info):
    # {'user_agent':user_agent,'browser':browser,'version':version,'platform':platform}
    blockName = ""
    if ":" in formName:
        blockName = formName.split(":")[0]
        formName = formName.split(":")[1]
    cmpDirSrc =  os.path.join(ROOT_DIR,get_option("TempDir", "temp/"))  # f'{ROOT_DIR}{get_option("TempDir", "temp/")}' # .replace("/",os.sep)
    cmpFiletmp =os.path.join(cmpDirSrc,agent_info['platform'],f"{formName.replace(os.sep, '_')}{blockName}.frm")   # f"{cmpDirSrc}{os.sep}{agent_info['platform']}_{formName.replace(os.sep, '_')}{blockName}.frm"
    if not os.path.exists(cmpDirSrc):
        os.makedirs(cmpDirSrc)
    txt = ""
    if existTempPage(cmpFiletmp):
        txt, mime = getTempPage(cmpFiletmp, '')
    if not txt == "":
        return txt
    if not os.path.exists(cmpFiletmp):
        print(os.path.dirname(cmpFiletmp))
        if not os.path.exists(os.path.dirname(cmpFiletmp)):
            os.makedirs(os.path.dirname(cmpFiletmp))
        with open(cmpFiletmp, "wb") as d3_css:
            txt = getSrc(formName, cache, dataSetName, agent_info)
            d3_css.write(txt.encode())
            setTempPage(cmpFiletmp, txt)
            return txt
    else:
        with open(cmpFiletmp, "rb") as infile:
            txt = infile.read()
            setTempPage(cmpFiletmp, txt)
            return txt


def getParsedForm(formName, cache, dataSetName="", agent_info={}):
    """
      Функция предназаначенна дла  чтения исходного файла формы и замены его фрагментов на компоненты
      !!!  необходимо переписать, и добавить логику DFRM (частичног опереопределения XML формы)
    """
    if get_option("TempDir") and (+get_option("debug")) < 1:
        return getTemp(formName, cache, dataSetName, agent_info)
    else:
        return getSrc(formName, cache, dataSetName, agent_info)


def parseVar(paramsQuery, dataSetXml, typeQuery, sessionObj):
    """
    Инициализируем объекта переменных из входных параметров запросов , сессии и значений по умолчанию
    """
    argsQuery = {}
    sessionVar = []
    for dataSetVarXml in dataSetXml.findall(f'cmp{typeQuery}Var'):
        key = dataSetVarXml.attrib.get("name")
        # default = dataSetVarXml.attrib.get("default") or ""
        # print(key,dataSetVarXml.tag ,dataSetVarXml.attrib.get("srctype"))
        if dataSetVarXml.attrib.get("srctype") == "session":
            if key in sessionObj:
                argsQuery[key] = sessionObj[key]
            else:
                if not dataSetVarXml.attrib.get("default") == None:
                    argsQuery[key] = dataSetVarXml.attrib.get("default")
                else:
                    argsQuery[key] = ""
            sessionVar.append(key)
            continue

        if not dataSetVarXml.attrib.get("default") == None:
            argsQuery[key] = dataSetVarXml.attrib.get("default")

        if not dataSetVarXml.attrib.get("get") == None:
            if len(dataSetVarXml.attrib.get("get")) == 0:
                subKey = dataSetVarXml.attrib.get("name")
                if paramsQuery.get(subKey) == None:
                    argsQuery[key] = ""
                else:
                    argsQuery[key] = paramsQuery.get(subKey)
                    del paramsQuery[subKey]
            else:
                subKey = dataSetVarXml.attrib.get("get")
                argsQuery[key] = paramsQuery.get(subKey)
                del paramsQuery[subKey]
        elif not dataSetVarXml.attrib.get("put") == None:
            if dataSetVarXml.attrib.get("get") == None or len(dataSetVarXml.attrib.get("get")) == 0:
                subKey = dataSetVarXml.attrib.get("name")
                if paramsQuery.get(subKey) == None:
                    argsQuery[key] = ""
                else:
                    argsQuery[key] = paramsQuery.get(subKey)
                    del paramsQuery[subKey]
            else:
                subKey = dataSetVarXml.attrib.get("get")
                argsQuery[key] = paramsQuery.get(subKey)
                del paramsQuery[subKey]
    for key in paramsQuery:
        argsQuery[key] = paramsQuery[key]
    return argsQuery, sessionVar


def joinDfrm(formName,rootForm):
    """
    Обработать DFRM и FRM
    Необходимо дописать замену найденой ноды на ноду из DFRM
    """
    pathUserFormDir = f"{USER_FORM_PATH}{os.sep}{formName}.d"
    if os.path.exists(pathUserFormDir):
        filesArr = [os.path.join(pathUserFormDir, fileName) for fileName in os.listdir(pathUserFormDir) if
                    fileName[-4:] == "dfrm"]
        xmldfrmtext = []
        for fileName in filesArr:
            xmldfrmtext.append(readFile(fileName))
        rootDfrmForm = ET.fromstring(f'<?xml version="1.0" encoding="UTF-8" ?><div>\n{"".join(xmldfrmtext)}</div>')
        for nodeXml in rootDfrmForm.iter(f'node'):
            findName = nodeXml.attrib.get("target")
            pos = nodeXml.attrib.get("pos")
            nodForm = None
            if "name" in rootForm.attrib:
                if rootForm.attrib.get('name') == findName:
                    nodForm = rootForm
            if nodForm == None:
                nodForm = rootForm.find(f"./*[@name='{findName}']")
            if nodForm == None:
                continue
            if pos == None:
                continue
            if pos == "del":
                rootForm.remove(nodForm)
            if pos == "after":
                fragArr = []
                for appEl in nodeXml.findall("*"):
                    # nodForm.append(appEl)
                    # nodForm.insert(0, appEl)
                    fragArr.append((ET.tostring(appEl)).decode('UTF-8'))
                txt = " ".join(fragArr)
                children = ET.fromstring(f'''<root>{ET.tostring(nodForm).decode('UTF-8')}{txt}</root>''')
                nodForm.clear()
                nodForm.extend(children)
            if pos == "before":
                fragArr = []
                for appEl in nodeXml.findall("*"):
                    fragArr.append((ET.tostring(appEl)).decode('UTF-8'))
                txt = " ".join(fragArr)
                children = ET.fromstring(f'''<root>{txt}{ET.tostring(nodForm).decode('UTF-8')}</root>''')
                nodForm.clear()
                nodForm.extend(children)
            if pos == "replace":
                fragArr = []
                for appEl in nodeXml.findall("*"):
                   fragArr.append((ET.tostring(appEl)).decode('UTF-8'))
                txt = " ".join(fragArr)
                children = ET.fromstring(f'''<root>{txt}</root>''')
                nodForm.clear()
                nodForm.extend(children)
        for attrXml in rootDfrmForm.iter('attr'):
            findNameAttr = attrXml.attrib.get("target")
            nodSrcForm = None
            if "name" in rootForm.attrib:
                if rootForm.attrib.get('name') == findNameAttr:
                    nodSrcForm = rootForm
            if nodSrcForm == None:
                nodSrcForm = rootForm.find(f"./*[@name='{findNameAttr}']")
            pos = attrXml.attrib.get("pos")
            nameFrag = attrXml.attrib.get("name")
            value = attrXml.attrib.get("value")
            if nodSrcForm == None:
                continue
            if pos == "del":
                nodSrcForm.attrib.pop(nameFrag, None)
            if pos == "replace":
                nodSrcForm.attrib[nameFrag] = value
            if pos == "after":
                nodSrcForm.attrib[nameFrag] = f"{nodSrcForm.attrib.get(nameFrag)}{value}"
            if pos == "before":
                nodSrcForm.attrib[nameFrag] = f"{value}{nodSrcForm.attrib.get(nameFrag)}"
            if pos == "add":
                nodSrcForm.attrib[nameFrag] = value
    # print(ET.tostring(rootForm))
    # nodes = [nodeXml for nodeXml in rootDfrmForm.findall(f'node')]
    # nodes.extend([attrXml for attrXml in rootDfrmForm.findall(f'attr')])
    return rootForm

def readFile(pathForm):
    if not os.path.exists(pathForm):
        return f'<?xml version="1.0" encoding="UTF-8" ?>\n<error>Fragment "{pathForm}" not found </error>'
    with codecs.open(pathForm, 'r', encoding='utf8') as f:
        xmlContentSrc = f.read()
    return xmlContentSrc


def getXMLObject(formName):
    global TEMP_XML_PAGE
    # TEMP_DS_PAGE = {}
    blockName = ""
    if ":" in formName:
        blockName = formName.split(":")[1]
        formName = formName.split(":")[0]
    formName = formName.replace("/", os.sep)
    pathForm = f"{FORM_PATH}{os.sep}{formName}.frm"
    pathUserForm = f"{USER_FORM_PATH}{os.sep}{formName}.frm"
    if os.path.exists(pathUserForm):
        pathForm = pathUserForm
    # print(pathForm)
    xmlText = f'<?xml version="1.0" encoding="UTF-8" ?>\n{readFile(pathForm)}'
    rootForm = ET.fromstring(xmlText)
    rootForm = joinDfrm(formName,rootForm)

    if not blockName == "":  # получаем блок XML с именем blockName
        nodes = rootForm.findall(f"*[@name='{blockName}']")  # ишим фрагмент формы по атребуту имени
        if len(nodes) > 0:
            rootForm = nodes[0]
        else:
            rootForm = ET.fromstring(
                f'<?xml version="1.0" encoding="UTF-8" ?>\n<error>Fragment "{formName}" not found </error>')
    return rootForm


def dataSetQuery(formName, typeQuery, paramsQuery, sessionObj, agent_info):
    """
    Функция обработки запросов DataSet и Action с клиентских форм
    """
    dataSetName=""
    if ":" in formName:
        dataSetName = formName.split(":")[0]
        # formName = formName.split(":")[1]
    # print(formName, dataSetName, typeQuery, paramsQuery)
    resObject = {dataSetName: {"type": typeQuery, "data": [], "locals": {}, "position": 0, "rowcount": 0}}
    uid = ""
    if "_uid_" in paramsQuery:
        uid = paramsQuery["_uid_"]
        del paramsQuery["_uid_"]
    if len(dataSetName)==0:
        resObject = {"dataSetName": {"type": typeQuery, "data": [], "locals": {}, "position": 0, "rowcount": 0}}
        resObject["dataSetName"]["uid"] = uid
        resObject["dataSetName"]["error"] = "Имя блока не определено"
        return json.dumps(resObject)
    rootForm = getXMLObject(formName)
    for dataSetXml in rootForm.findall(f'cmp{typeQuery}'):
        if not "name" in dataSetXml.attrib:
            return f'{"error":"Не найден атрибут с именем"}'
        if not dataSetXml.attrib.get("name") == dataSetName:
            continue
        # =============== Вставляем инициализированые переменные =======================
        argsQuery, sessionVar = parseVar(paramsQuery, dataSetXml, typeQuery, sessionObj)
        varsDebug = {}
        if get_option("debug") > 0:
            varsDebug = argsQuery.copy()
        # =============================================================================
        if typeQuery == "Action":
            if "query_type" in dataSetXml.attrib:
                query_type = dataSetXml.attrib.get("query_type")
            if query_type == "server_python":  # выполнить Python скрипт
                code = stripCode(dataSetXml.text)
                dataVarReturn = {}
                localVariableTemp = {}
                try:
                    localVariableTemp = exec_then_eval(argsQuery, code, sessionObj)
                except:
                    resObject["error"] = f"{formName} : {dataSetName} :{sys.exc_info()}"
                for elementDict in localVariableTemp:
                    if elementDict[:2] == '__' or elementDict == 'elementDict' \
                            or elementDict == 'localVariableTemp' or elementDict == 'sys':
                        continue
                    if elementDict in sessionVar:  # запоменаем переменные сессии
                        sessionObj[elementDict] = localVariableTemp[elementDict]
                    else:
                        dataVarReturn[elementDict] = localVariableTemp[elementDict]
                del localVariableTemp
                resObject[dataSetName]["data"] = dataVarReturn
                resObject[dataSetName]["type"] = typeQuery
                resObject[dataSetName]["uid"] = uid
                if get_option("debug") > 0:
                    resObject[dataSetName]["var"] = varsDebug
                    resObject[dataSetName]["sql"] = [line for line in code.split("\n")]
                return json.dumps(resObject)

        if typeQuery == "DataSet":
            query_type = "sql"
            if "query_type" in dataSetXml.attrib:
                query_type = dataSetXml.attrib.get("query_type")
            if query_type == "server_python":  # выполнить Python скрипт
                code = stripCode(dataSetXml.text)
                dataVarReturn = {}
                localVariableTemp = {}
                try:
                    localVariableTemp = exec_then_eval(argsQuery, code, sessionObj)
                except:
                    resObject["error"] = f"{formName} : {dataSetName} :{sys.exc_info()}"
                for elementDict in localVariableTemp:
                    if elementDict[:2] == '__' or elementDict == 'elementDict' \
                            or elementDict == 'localVariableTemp' or elementDict == 'sys':
                        continue
                    if elementDict in sessionVar:  # запоменаем переменные сессии
                        sessionObj[elementDict] = localVariableTemp[elementDict]
                    else:
                        dataVarReturn[elementDict] = localVariableTemp[elementDict]
                del localVariableTemp
                if "data" in dataVarReturn:
                    resObject[dataSetName]["data"] = dataVarReturn["data"]
                    resObject[dataSetName]["rowcount"] = len(dataVarReturn["data"])
                    del dataVarReturn["data"]
                resObject[dataSetName]["rowcount"] = len(resObject[dataSetName]["data"])
                if "position" in dataVarReturn:
                    resObject[dataSetName]["rowcount"] = dataVarReturn['position']
                    del dataVarReturn['position']
                if "rowcount" in dataVarReturn:
                    resObject[dataSetName]["rowcount"] = dataVarReturn['rowcount']
                    del dataVarReturn['rowcount']
                resObject[dataSetName]["locals"] = dataVarReturn
                resObject[dataSetName]["uid"] = uid
                resObject[dataSetName]["type"] = typeQuery
                resObject[dataSetName]["position"] = 0
                resObject[dataSetName]["page"] = 0
                if get_option("debug") > 0:
                    resObject[dataSetName]["var"] = varsDebug
                    resObject[dataSetName]["sql"] = [line for line in code.split("\n")]

                return json.dumps(resObject)
            else:
                # дописать обработку SQL запроса
                s = {dataSetName: {"type": typeQuery, "data": [{'console': "Необходимо допилить метод"}], "locals": {},
                                   "position": 0, "rowcount": 0}}
                return json.dumps(s)
    s = {dataSetName: {"type": typeQuery, "data": [{'console': "Необходимо допилить метод"}], "locals": {},
                       "position": 0, "rowcount": 0}}
    return json.dumps(s)


"""

DataSet
{
  "type": "DataSet",
  "uid": "DS2471634288781925",
  "data": [
    {
      "ID": "556277290",
      "FULLNAME": "ЛПУ для тренироваки"
    }
  ],
  "position": 0,
  "rowcount": 914,
  "page": 0
}

def parseFrm(root):
    attrib = root.attrib.copy()
    if len(root.attrib) > 0:
        data = " ".join(f'{k}="{v}"' for k, v in root.attrib.items())
    else:
        data = ""
    if not root.text == None and root.tail == None:
        print(f"<{root.tag}{data}>", end="")
        print(root.text, end="")

    elif root.text == None and not root.tail == None:
        # если тэг закрытый
        print(f"<{root.tag}{data}/>", end="")

    elif not root.text == None and not root.tail == None:
        print(f"<{root.tag}{data}>", end="")
        print(root.text, end="")
    else:
        pass
        # print(root.text)

    # =========== Рекурсионый обход дерева ============================
    if hasattr(root, 'getchildren'):
        for elem in root.getchildren():
            parseFrm(elem)
    elif len(root) > 0:
        for elem in root:
            parseFrm(elem)
    # =================================================================
    if not root.text == None and root.tail == None:
        print(f"</{root.tag}>", end="")
    elif root.text == None and not root.tail == None:
        print(root.tail, end="")
    elif not root.text == None and not root.tail == None:
        # print(root.tail)
        # print(root.text)
        print(f"</{root.tag}>", end="")
        print(root.tail, end="")
"""
