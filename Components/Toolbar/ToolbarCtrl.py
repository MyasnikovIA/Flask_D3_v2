from Components.Base.BaseCtrl import *


class Toolbar(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Toolbar'
        self.tag = 'div'
        self.tagCls="</div></div>"

        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        self.classCSS = ["toolbarCtrl"]
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']

        self.onchange = ""
        if 'onchange' in self.attrs:
            self.onchange = self.attrs['onchange']
            del self.attrs['onchange']
        self.caption = ""
        if 'caption' in self.attrs:
            self.caption = self.attrs['caption']
            del self.attrs['caption']


    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt=""
        if len(self.styleArr)>0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """

        classStr = ""
        if len(self.classCSS)>0:
            classStr = f' class="{" ".join(self.classCSS)}" '

        self.print(f"""
<div name="{self.name}" cmptype="Toolbar" {atr} {classStr} {atr} onchange="{self.onchange};D3Api.ToolbarCtrl.onChangeToolbar(this);" id="d3ctrl{self.genName()}" {stleTxt} {eventsStr}>
    <div class="toolbarCtrl_container">
        <span class="header">{ self.caption}</span>
""" )

        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Image/js/Image.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Image/css/Image.css</cssfile>")
