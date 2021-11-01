from Components.Base.BaseCtrl import *

class TabSheet(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'TabSheet'
        self.tag = 'div'
        if "text" in self.attrs:
            self.text = self.attrs["text"]
            del self.attrs["text"]
        else:
            self.text = ""

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>\n""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/TabSheet/js/TabSheet.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/TabSheet/css/TabSheet.css</cssfile>")

