from Components.Base.BaseCtrl import *

class TabsItem(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'TabsItem'
        self.tagCls = "</section>"
        self.tag = 'section'
        if "text" in self.attrs:
            self.text = self.attrs["text"]
            del self.attrs["text"]
        else:
            self.text = ""

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<section id="content-tab2" cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>\n""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/TabsItem/js/TabsItem.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/TabsItem/css/TabsItem.css</cssfile>")

