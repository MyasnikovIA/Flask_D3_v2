from Components.Base.BaseCtrl import *

class DataSetVar(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = '';
        self.tag = '';
        self.SysInfoTag = 'Var'

        if "srctype" in self.attrs:
            self.srctype = self.attrs.get("srctype")
        else:
            self.srctype = "var"

        if "src" in self.attrs:
            self.src = self.attrs.get("src")
        else:
            self.src = self.name

        if "put" in self.attrs:
            if  not self.attrs.get('put') == None:
                self.getput = f"put='{self.attrs.get('put')}'"
            else:
                self.getput = f"put='{self.name}'"
        elif not self.attrs.get('get') == None:
            self.getput = f"get='{self.attrs.get('get')}'"
        else:
            self.getput =f"get='{self.name}'"

    def show(self):
        # подгрузка библитек
        self.SetSysInfo.append(f'<Var {self.getput}  src="{self.src}" srctype="{self.srctype}">')
        # self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")
