from Components.Base.BaseCtrl import *

class Script(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Script';
        self.tag = 'textarea';

    def show(self):
        self.print(f"""<{self.tag} cmptype={self.CmpType} name="{self.name}" style="display:none;">""")
        # подгрузка библитек
        # self.SetSysInfo.append("<scriptfile>Components/Script/js/Script.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Script/css/Script.css</cssfile>")
