from Components.Base.BaseCtrl import *


class TextArea(Base):
    """
       <div  name="myTest" cmptype="TextArea" title="" class="textArea box-sizing-force editControl" >
           <textarea cmpparse="TextArea" >sadfasdfasdf</textarea>
       </div>
    """
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'TextArea';
        self.tag = 'div';
        self.placeholder = getDomAttrRemove('placeholder', None, self.attrs);

        # ============== INIT Html style =========================
        self.styleArr = []
        if 'style'in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']
        # ============== INIT Html Class =========================
        # textArea box-sizing-force editControl

        self.classCSS = ['textArea', 'box-sizing-force', 'editControl']
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']
        # ========================================================

        self.onclick = ""
        if 'onclick' in self.attrs:
            self.onclick = f' onclick="{self.attrs["onclick"]}" '
            del self.attrs['onclick']
        self.onchange = ""
        if 'onchange' in self.attrs:
            self.onchange = f' onchange="{self.attrs["onchange"]}" '
            del self.attrs['onchange']
        self.onkeypress = ""
        if 'onkeypress' in self.attrs:
            self.onkeypress = f' onkeypress="{self.attrs["onkeypress"]}" '
            del self.attrs['onkeypress']
        self.onkeyup = ""
        if 'onkeyup' in self.attrs:
            self.onkeyup = f' onkeyup="{self.attrs["onkeyup"]}" '
            del self.attrs['onkeyup']
        self.onkeydown = ""
        if 'onkeydown' in self.attrs:
            self.onkeydown = f' onkeydown="{self.attrs["onkeydown"]}" '
            del self.attrs['onkeydown']
        if 'width' in self.attrs:
            self.styleArr.append(f'width:{self.attrs["width"]}')
            del self.attrs['width']
        if 'height' in self.attrs:
            self.styleArr.append(f'height:{self.attrs["height"]}')
            del self.attrs['height']
    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        stleTxt=""
        if len(self.styleArr)>0:
            stleTxt = f"""style="{';'.join(self.styleArr)}" """
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items())
        self.print(f"""
        <div  name="{self.name}" cmptype="{ self.CmpType }" title="" class="{' '.join(self.classCSS)}" {stleTxt} {atr} {eventsStr}>
           <textarea cmpparse="{ self.CmpType }" {self.placeholder} {self.onclick}{self.onchange}{self.onkeypress}{self.onkeyup}{self.onkeydown} >{self.value}</textarea>
        """)
        # подгрузка библитек
        # self.SetSysInfo.append("<scriptfile>Components/TextArea/js/TextArea.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/TextArea/css/TextArea.css</cssfile>")

