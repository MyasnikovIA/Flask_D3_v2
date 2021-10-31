import uuid
import random
from datetime import datetime
from Etc.conf import get_option
from getform import parseFrm,getXMLObject
import re
import os

class Base:
    def __init__(self, attrs):
        self.isDebug = int(get_option("debug", 0))

        # Имя формы на которой расположен элемент
        if "formName" in attrs:
            self.formName = attrs["formName"]
            del attrs["formName"]
        else:
            self.formName = ""

        if "title" in attrs:
            self.title = attrs["title"]
            del attrs["title"]
        else:
            self.title = ""

        if "value" in attrs:
            self.value = attrs["value"]
            del attrs["value"]
        else:
            self.value = ""

        if "readonly" in attrs:
            self.readonly = attrs["readonly"]
            del attrs["readonly"]
        else:
            self.readonly = ""

        if "disabled" in attrs:
            self.disabled = attrs["disabled"]
            del attrs["disabled"]
        else:
            self.disabled = ""

        if "tag" in attrs:
            self.tag = attrs["tag"]
            del attrs["tag"]
        else:
            self.tag = ""

        if "tagName" in attrs:
            self.tagName = attrs["tagName"]
            del attrs["tagName"]
        else:
            self.tagName = "div"

        if 'cmptype' in attrs:
            self.CmpType = attrs['cmptype']
            del attrs['cmptype']
        else:
            self.CmpType = ""

        if 'name' in attrs:
            self.name = attrs['name']
            del attrs['name']
        else:
            self.name = self.genName()

        # Содержимое innerHTML (после тэга следующего элемента)
        if "tail" in attrs:
            self.tail = attrs["tail"]
            del attrs["tail"]
        else:
            self.tail = ""

        # Содержимое innerHTML (до тэга следующего элемента)
        if 'text' in attrs:
            self.innerHTML = attrs['text']
            self.text = attrs['text']
        else:
            self.innerHTML = ""
            self.text = ""

        #  Родительский элемент XML
        if 'parentElement' in attrs:
            self.parentElement = attrs['parentElement']
            del attrs['parentElement']
        else:
            self.parentElement = {}

        #  Элемент XML SRC
        if 'nodeXML' in attrs:
            self.nodeXML = attrs['nodeXML']
            del attrs['nodeXML']
        else:
            self.nodeXML = None

        # Последовательный номер элемента
        if 'num_element' in attrs:
            self.num_element = attrs['num_element']
            del attrs['num_element']
        else:
            self.num_element = 0

        # информация о подключаемом устройстве
        if 'session' in attrs:
            self.session = attrs['session']
            del attrs['session']
        else:
            self.session = {}

        self.attrs = attrs
        self.SetSysInfo = []
        self.HTML_DST = []

    def show(self):
        pass

    def print(self, text, end=""):
        self.HTML_DST.append(text)
        self.HTML_DST.append(end)

    def genName(self):
        """
        генерируем случайное число на основании даты + случайное число + имени формы
        """
        return str(uuid.uuid5(uuid.NAMESPACE_DNS,
                              f"{datetime.now().microsecond}{random.randint(0, 9999999)}{self.formName}")).replace("-",
                                                                                                                   "")


class BaseCtrl(Base):

    def __init__(self, attrs, parent):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'Base';
        self.tag = '<sa>';
        self.formInfo = ""
        if self.isDebug > 0:
            self.formInfo = f""" formName="{self.formName}" """

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr} {self.formInfo}>""")
        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/Base/js/Base.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Base/css/Base.css</cssfile>")


def getDomAttr(name, value='', attrs=None):
    if attrs != None:
        v = ArrKeyRtrn(attrs, name);
        if len(v) > 0:
            value = v
        if len(v) == 0 and value == None:
            return ''
    if value == 'true':
        value = name
    value = value.replace("'", "\'")
    return f""" {name} = '{value}' """


def getDomAttrRemove(name, value='', attrs=None):

    if name in attrs:
        val = attrs[name]
        if len(val)==0 and not value == None:
            val = value
        if val == 'true':
            val = name
        val = val.replace("\"", "\\\"")
        del attrs[name]
        return f""" {name} = "{val}" """
    else:
        if not value == None:
            return f""" {name} = "{value}" """
        else:
            return ""


def RemoveArrKeyRtrn(arr, key, default=''):
    if key in arr:
        value = arr[key]
        del arr[key]
        return value
    else:
        return default


def ArrKeyRtrn(arr, key, default=''):
    if key in arr:
        value = arr[key]
        return value
    else:
        return default


def getBooleanAttr(name, attrs, default, remove=True):
    if name not in attrs:
        return default;

    res = attrs[name] == 'true' or attrs[name] == name;
    if (remove):
        del attrs[name]
    if res:
        return 'true'
    else:
        return ''


def RemoveArrKeyCondition(arr, condition='on'):
    return {k[v] for k, v in arr.items() if k[:2] == condition}


def str_replace(elsrctxt, eldsttxt, txt):
    return txt.replace(elsrctxt, eldsttxt)
