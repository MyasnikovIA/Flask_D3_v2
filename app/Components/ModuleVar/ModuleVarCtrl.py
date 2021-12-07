from Components.Base.BaseCtrl import *


class ModuleVar(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.SysInfoTag = 'var';
        self.CmpType = 'Script';
        self.tag = '';

        if "src" in self.attrs:
            self.src = self.attrs.get("src")
        else:
            self.src = self.name

        if "srctype" in self.attrs:
            self.srctype = self.attrs.get("srctype")
        else:
            self.srctype = "var"

        self.getput = f"get='{self.name}'"

        if not self.attrs.get('get') == None:
            if len(self.attrs.get('get')) == 0:
                self.getput = f"get='{self.name}'"
            else:
                self.getput = f"get='{self.attrs.get('get')}'"

        if not self.attrs.get('put') == None:
            if len(self.attrs.get('put')) == 0:
                self.getput = f"put='{self.name}'"
            else:
                self.getput = f"put='{self.attrs.get('put')}'"

    def show(self):
        self.SetSysInfo.append(f'\n<var {self.getput} src="{self.src}" srctype="{self.srctype}">')

        # подгрузка библитек
        # self.SetSysInfo.append("<scriptfile>Components/Label/js/Label.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")
