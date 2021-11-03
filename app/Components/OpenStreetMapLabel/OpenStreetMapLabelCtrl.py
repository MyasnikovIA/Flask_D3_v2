from Components.Base.BaseCtrl import *


class OpenStreetMapLabel(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'OpenStreetMapLabel'
        self.tag = 'div'
        self.tagCls="</div></div>"

        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        if 'bottom' in self.attrs:
            # self.styleArr.extend(["position: absolute","right: -10px",'left: 10px','bottom: 10px']);
            self.styleArr.append("position: absolute")
            self.styleArr.append("right:10px")
            self.styleArr.append('left: 10px')
            self.styleArr.append('bottom: 10px')
            # del self.attrs['bottom']

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
        if 'text' in self.attrs:
            del self.attrs['text']



    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt=""
        if len(self.styleArr)>0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """

        classStr = ""
        if len(self.classCSS)>0:
            classStr = f' class="{" ".join(self.classCSS)}" '
        captText=""
        if len(self.caption)>0:
            captText = f'<span class="header">{self.caption}</span>'



        self.print(f"""
<div name="{self.name}" cmptype="Toolbar" {atr} {classStr} {atr} onchange="{self.onchange};D3Api.ToolbarCtrl.onChangeToolbar(this);" id="d3ctrl{self.genName()}" {stleTxt} {eventsStr}>
    <div class="toolbarCtrl_container">
        {captText}
""" )

        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Toolbar/js/Toolbar.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Toolbar/css/Toolbar.css</cssfile>")
