from Components.Base.BaseCtrl import *

class Form(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'Base';
        self.tag = 'div';

    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Form/js/Form.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Form/css/Form.css</cssfile>")



