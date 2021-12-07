from Components.Base.BaseCtrl import *

class html(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        if self.tag == "script":
            self.text = ""
            self.tagCls = "</script>"

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        skipPar = ["session",'tagName', 'nodeXML','parentElement','num_element','text']
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on" and not k in skipPar)
        self.print(f"""<{self.tag}  {atr}  {eventsStr}>""")
