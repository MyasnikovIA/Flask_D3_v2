from Components.Base.BaseCtrl import *

class SubForm(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Dialog';
        self.tagCls = "</div>"
        self.tag = 'div';
        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']
        if 'class' not in self.attrs:
            self.classCSS = []
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']

        self.path = ""
        if 'path' in self.attrs:
            self.path = self.attrs["path"]
            del self.attrs['path']

    def show(self):
        if self.path == "":
            return None
        rootForm = getXMLObject(self.path)
        sysinfoBlock, htmlContent = parseFrm(rootForm, self.path, {}, 0)  # парсим форму
        self.print(htmlContent)
        # Добавляется при инициализации  d3main.js d3theme.css
        self.SetSysInfo.extend(sysinfoBlock)
