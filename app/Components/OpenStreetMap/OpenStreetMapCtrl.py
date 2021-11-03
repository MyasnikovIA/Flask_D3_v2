from Components.Base.BaseCtrl import *


class OpenStreetMap(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'OpenStreetMap'
        self.tag = 'div'
        self.tagCls = "</div>"
        self.classCSS = ['textArea', 'box-sizing-force', 'editControl']
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']

        if 'caption' in self.attrs:
            self.caption = self.attrs['caption']
            del self.attrs['caption']
        self.uniqid = self.genName()

        self.filtr = ""
        if 'filtr' in self.attrs:
            self.filtr = f"""<input type="text" value="" id="FoundGroObject{self.uniqid}" onkeydown="if (event.keyCode == 13){{ D3Api.OpenStreetMapCtrl.getGisObjest(this.value); }}"> """
            del self.attrs['filtr']
        self.onclick = ""
        if 'onclick' in self.attrs:
            self.onclick = f""" onclick=" {self.attrs['onclick']} ;"  """
            del self.attrs['onclick']
        self.styleArr = []

        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']
        if 'width' in self.attrs:
            self.styleArr.append(f"width:{self.attrs['width']}")
            del self.attrs['width']
        if 'height' in self.attrs:
            self.styleArr.append(f"height:{self.attrs['height']}")
            del self.attrs['height']



    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on" )
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt = ""
        if len(self.styleArr)>0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """


        self.print(f"""<div   cmptype="{self.CmpType}" name="{self.name}"  {eventsStr} {self.onclick}   class="{' '.join(self.classCSS)}" uniqid="{self.uniqid}" {atr} {stleTxt} >
                {self.filtr}
                <div id='basicMap{self.uniqid}' class="MapContent{self.uniqid}"></div>
        """)

        # self.SetSysInfo.append("<scriptfile>/Components/OpenStreetMap/js/OpenLayers.js</scriptfile>")
        self.SetSysInfo.append("<scriptfile>Components/OpenStreetMap/js/OpenLayers.js</scriptfile>") # в локальной версии исправлена ошибка при  увеличении масштаба
        self.SetSysInfo.append("<cssfile>Components/OpenStreetMap/css/OpenStreetMap.css</cssfile>")
        # подключаем библиотеку из интернета
        # self.SetSysInfo.append("<scriptfile>https://openlayers.org/api/2.13.1/OpenLayers.js</scriptfile>")
