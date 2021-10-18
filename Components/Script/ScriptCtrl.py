from Components.Base.BaseCtrl import *

class Script(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Script';
        self.tag = 'textarea';

    def show(self):
        self.print(f"""<{self.tag} cmptype={self.CmpType} name="{self.name}" style="display:none;"> {self.text}""")
        # подгрузка библитек
        # self.SetSysInfo.append("<scriptfile>Components/Label/js/Label.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")
