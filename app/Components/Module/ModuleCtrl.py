from Components.Base.BaseCtrl import *

"""
<Action name="getInfoCount">
    <var get="g0" src="DEP_SEL" srctype="ctrl"></var>
    <var put="p0" src="IS_HIDE_CLOSED" srctype="ctrl"></var>
    <var put="p1" src="NUMBER_OF_EXEMINATIONS:caption" srctype="ctrl"></var>
    <var put="p2" src="AMOUNT_TO_BE_AGREED:caption" srctype="ctrl"></var>
    <var put="p3" src="NUMBER_OF_NEW_EXEMINATIONS:caption" srctype="ctrl"></var>
    <var put="p4" src="REGISTERED_TODAY:caption" srctype="ctrl"></var>
    <var put="p5" src="SUSPENDED:caption" srctype="ctrl"></var>
    <var put="p6" src="COMPLETED_TODAY:caption" srctype="ctrl"></var>
</Action>
"""

class Module(Base):


    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = '';
        self.tag = '';
        self.SysInfoTag = 'Module';
        if "get" in self.attrs:
            self.get = self.attrs.get
        else:
            self.get = f"v{self.name}"


        if "activateoncreate" in self.attrs:
            self.activateoncreate = self.attrs.get("activateoncreate")
        else:
            self.activateoncreate = "true"
        self.text = ""

    def show(self):
        # подгрузка библитек
        self.SetSysInfo.append(f'\r<Module name="{self.name}"  activateoncreate="{self.activateoncreate}">\r')
        # self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")
