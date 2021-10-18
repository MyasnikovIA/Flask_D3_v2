from Components.Base.BaseCtrl import *

class DataSet(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = '';
        self.tag = '';
        self.SysInfoTag = 'DataSet';

        if "get" in self.attrs:
            self.get = self.attrs.get
        else:
            self.get ="v{self.name}"
        if "Range" in self.attrs:
            self.Range = self.attrs.Range
        else:
            self.Range = "Range"

        if "activateoncreate" in self.attrs:
            self.activateoncreate = self.attrs.get("activateoncreate")
        else:
            self.activateoncreate = "true"

    def show(self):
        # подгрузка библитек
        self.SetSysInfo.append(f'<DataSet name="{self.name}" mode="{self.Range}" activateoncreate="{self.activateoncreate}">')
        # self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")
