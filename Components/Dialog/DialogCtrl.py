from Components.Base.BaseCtrl import *

# для получения  Фрагмента формы необходимо написать обработку нового атребута blockName
# Указываем имя блока , который должны получить
# http://192.168.15.200:9091/getform.php?cache_enabled=0&modal=1&Form=Tutorial%2FDialog%2FDialog&cache=c865f9af408fb94ce38db76e0b211b032&blockName=d_wg_delete_Ctrl

class Dialog(Base):
    """
    Дописать компонент
    """
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Dialog';
        self.tagCls = ""
        self.tag = ''
        self.nodeXML.tag = "div"
        self.styleArr=[]
        if 'style'in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        if 'class' not in self.attrs:
            self.classCSS = []
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']
        if str(self.parentElement) == "{}":  # если элемент вызывается как отдельный фрагмент
          pass

        else:  # если элемент вызывается всемте  с формой, тогда очищаем содержимое элемента
            #  Очищаем содержимое блока
            for element in  self.nodeXML.findall('*'):
                self.nodeXML.remove(element)

    def show(self):
        if str(self.parentElement) == "{}": # если элемент вызывается как отдельный фрагмент
            self.print(f"""<div name="{self.name}" cmptype="Dialog"/>""")
        else:  # если элемент вызывается всемте  с формой, тогда пропускаем его
            self.print(f"""<div name="{self.name}" cmptype="Dialog"/>""")
        #sysinfoBlock, htmlContent = parseFrm(self.nodeXML,self.formName,{},0)
        #self.print(htmlContent)
        ## Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.extend(sysinfoBlock)
