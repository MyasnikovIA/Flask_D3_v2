from Components.Base.BaseCtrl import *


class HyperLink(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'HyperLink';
        self.tag = 'a';
        if not "onclick" in self.attrs:
            self.controls = ' onclick = "D3Api.HyperLinkCtrl.onClick(this);" '
        else:
            self.controls = f""" onclick = "{self.attrs["onclick"]}" """
            del self.attrs["onclick"]
        if not "class" in self.attrs:
            self.classStr = ' class = "ctrl_hyper_link" '
        else:
            self.classStr = f""" class="{self.attrs["class"]} ctrl_hyper_link" """
            del self.attrs["class"]
        if not "style" in self.attrs:
            self.style = ''
        else:
            self.style = f""" style="{self.attrs["style"]}" """
            del self.attrs["style"]


    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<a  cmptype="{self.CmpType}" tabindex="0" name="{self.name}" {eventsStr}{atr} {self.classStr} {self.style}>{self.caption}{self.text}""" )
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Mask/js/Mask.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Mask/css/Mask.css</cssfile>")
