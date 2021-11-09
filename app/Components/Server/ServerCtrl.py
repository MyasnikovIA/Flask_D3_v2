from Components.Base.BaseCtrl import *

class Server(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = ''
        self.tag = ''
        self.text = ''

    def show(self):
        # очистка содержимого блока
        for element in self.nodeXML.findall('*'):
            self.nodeXML.remove(element)
        # подгрузка библитек
        # self.SetSysInfo.append("<scriptfile>Components/Server/js/Server.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Server/css/Server.css</cssfile>")
