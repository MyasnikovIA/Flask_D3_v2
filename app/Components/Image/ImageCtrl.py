from Components.Base.BaseCtrl import *


class Image(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Image';
        self.tag = '';
        if not "onclick" in self.attrs:
            self.controls = ' onclick = "D3Api.HyperLinkCtrl.onClick(this);" '
        else:
            self.controls = f""" onclick = "{self.attrs["onclick"]}" """
            del self.attrs["onclick"]

        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        self.classCSS = ["D3Image"]
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']

        if "src" not in self.attrs:
            self.classCSS.append('ctrl_hidden')

        self.tabindex = ""
        if "tabindex" in self.attrs:
            self.tabindex = f' tabindex="{self.attrs["tabindex"]}" '
            del self.attrs["tabindex"]


    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt=""
        if len(self.styleArr)>0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """

        classStr = ""
        if len(self.classCSS)>0:
            classStr = f' class="{" ".join(self.classCSS)}" '

        self.print(f"""<img  cmptype="{self.CmpType}" {self.tabindex} name="{self.name}" {eventsStr} {atr} {classStr} {stleTxt}/>""" )
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Image/js/Image.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Image/css/Image.css</cssfile>")
