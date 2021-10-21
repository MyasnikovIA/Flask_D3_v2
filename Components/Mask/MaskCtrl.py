
from Components.Base.BaseCtrl import *


class Mask(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Mask';
        self.tag = 'div';
        if not "controls" in self.attrs:
            self.controls = ""
        else:
            self.controls = f""" controls = "{self.attrs["controls"]}" """
            del self.attrs["controls"]


    def show(self):
        self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {self.controls}  style="display:none" >""" )
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Mask/js/Mask.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Mask/css/Mask.css</cssfile>")

