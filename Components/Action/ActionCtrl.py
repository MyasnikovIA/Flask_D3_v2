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

class Action(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = '';
        self.tag = '';
        self.SysInfoTag = 'Action';
        if "get" in self.attrs:
            self.get = self.attrs.get
        else:
            self.get ="v{self.name}"
        if "Range" in self.attrs:
            self.Range = self.attrs.Range
        else:
            self.Range = "Range"
        if "activateoncreate" in self.attrs:
            self.activateoncreate = self.attrs.activateoncreate
        else:
            self.activateoncreate = "true"
        if self.isDebug > 0:
            self.text = f"""<!-- Action="{self.name}"  formName="{self.formName}"  {self.text}  -->"""
        else:
            self.text = ""

    def show(self):
        # подгрузка библитек
        self.SetSysInfo.append( f'<Action name="{self.name}" activateoncreate="{self.activateoncreate}">')
