from Components.Base.BaseCtrl import *


class ToolbarItemGroup(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'ToolbarItemGroup'
        self.tag = 'span'
        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        self.classCSS = ["toolbarItemGroup"]
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']
        if 'align' in self.attrs:
            self.classCSS.append(self.attrs['align'])
            del self.attrs['align']

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt = ""
        if len(self.styleArr) > 0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """

        classStr = ""
        if len(self.classCSS) > 0:
            classStr = f' class="{" ".join(self.classCSS)}" '

        self.print(f"""<span  name="{self.name}" cmptype="toolbarItemGroup" {classStr} id="d3ctrl{self.genName()}" {stleTxt} {eventsStr} {atr} > """)
        #self.print(f"""<span  name="{self.name}" cmptype="ToolbarItemGroup" {classStr} id="d3ctrl{self.genName()}" {stleTxt} {eventsStr} {atr} > """)

        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/Image/js/Image.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Image/css/Image.css</cssfile>")
