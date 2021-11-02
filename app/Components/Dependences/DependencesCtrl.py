from Components.Base.BaseCtrl import *


class Dependences(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Dependences';
        self.tag = 'div';
        if not "depend" in self.attrs:
            self.depend = ""
        else:
            self.depend = f""" depend = "{self.attrs["depend"]}" """
            del self.attrs["depend"]

        if not "required" in self.attrs:
            self.required = ""
        else:
            self.required = f""" required = "{self.attrs["required"]}" """
            del self.attrs["required"]

        if not "repeatername" in self.attrs:
            self.repeatername = ""
        else:
            self.repeatername = f""" repeatername = "{self.attrs["repeatername"]}" """
            del self.attrs["repeatername"]

        if not "condition" in self.attrs:
            self.condition = ""
        else:
            self.condition = f""" condition = "{self.attrs["condition"]}" """
            del self.attrs["condition"]

    def show(self):
        self.print(
            f"""<div  cmptype="{self.CmpType}" name="{self.name}"{self.depend}{self.required}{self.repeatername}{self.condition}  style="display:none" >""")
        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/Dependences/js/Dependences.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Dependences/css/Dependences.css</cssfile>")
