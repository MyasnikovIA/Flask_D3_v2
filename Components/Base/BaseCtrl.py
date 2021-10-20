import uuid
from Etc.conf import get_option

class Base:
    def __init__(self, attrs):
        self.isDebug = int(get_option("debug", 0))
        if "formName" in attrs:
            self.formName = attrs["formName"]
            del attrs["formName"]
        else:
            self.formName = ""
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

        if "text" in attrs:
            self.text = attrs["text"]
            del attrs["text"]
        else:
            self.text = ""
        if "tail" in attrs:
            self.tail = attrs["tail"]
            del attrs["tail"]
        else:
            self.tail = ""
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
        if 'text' in attrs:
            self.innerHTML = attrs['text']
        else:
            self.innerHTML = ""
        self.attrs = attrs
        self.SetSysInfo = []
        self.HTML_DST = []

    def show(self):
        pass

    def print(self, text, end=""):
        self.HTML_DST.append(text)
        self.HTML_DST.append(end)


class BaseCtrl(Base):

    def __init__(self, attrs, parent):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'Base';
        self.tag = '<sa>';
        self.formInfo=""
        if self.isDebug>0:
            self.formInfo = f""" formName="{self.formName}" """


    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")


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
    if attrs != None:
        v = RemoveArrKeyRtrn(attrs, name);
        if len(v) > 0:
            value = v
        if len(v) == 0 and value == None:
            return ''
    if value == 'true':
        value = name
    value = value.replace("'", "\'")
    return f""" {name} = '{value}' """


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
