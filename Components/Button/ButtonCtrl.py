from Components.Base.BaseCtrl import *

class Button(Base):

    """
    <div  onclick="Form.runDataSet()" cmptype="Button" name="cmp5f7b4c4706deb" title=""  tabindex="0" class="ctrl_button box-sizing-force" style="width: 255px;">
       <div class="btn_caption btn_center minwidth" >запустить runDataSet</div>
    </div>

    <button type="button" class="btn btn-primary">Primary</button>
    """

    def __init__(self,attrs):
        super().__init__(attrs)
        self.CmpType = 'Button';
        self.tag = 'div';
        self.events={}
        self.style = []
        self.classCSS = []
        if 'style' in attrs:
            self.style = [i for i in RemoveArrKeyRtrn(attrs, 'style').split(";")]
        # ====================================================
        # ====================================================
        # ====================================================
        self.nominwidth = RemoveArrKeyRtrn(self.attrs, 'nominwidth')
        self.popupmenu = RemoveArrKeyRtrn(self.attrs, 'popupmenu')
        self.caption = RemoveArrKeyRtrn(self.attrs, 'caption')
        # ============== ICON Button =========================
        self.icon = RemoveArrKeyRtrn(attrs, 'icon')
        if len(self.icon) > 0:
            self.icon = f'''<div class="btn_icon"><img src="{self.icon}" class="btn_icon_img"/></div>'''
        # ====================================================
        if ('onlyicon' in self.attrs) or (('caption' in self.attrs) and (len(attrs['caption'] == 0))):
            self.classCSS.append('onlyicon')
        # ============== INIT Html Class =========================


        if 'text' not in self.attrs:
            self.text =""
        else:
            self.text = self.attrs.get("text")

        if 'class' not in self.attrs:
            self.classCSS = ['ctrl_button', 'box-sizing-force']
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']
        if ('ctrl_button' not in self.classCSS):
            self.classCSS.append('ctrl_button')
        if ('box-sizing-force' not in self.classCSS):
            self.classCSS.append('box-sizing-force')
        # ========================================================
        if len(self.popupmenu) > 0 and ('onclick' not in self.attrs):
            self.attrs['onclick'] = f"D3Api.ButtonCtrl.showPopupMenu(this,'{self.popupmenu}');"
        elif len(self.popupmenu) > 0 and ('onclick' in self.attrs):
            self.attrs['onclick'] = f"""{self.attrs['onclick']} D3Api.ButtonCtrl.showPopupMenu(this,'{self.popupmenu}'); """
        self.data = getDomAttrRemove('data', None, self.attrs);


    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        if len(self.classCSS) > 0:
            classCSSStr = f""" class='{' '.join(self.classCSS)}'"""
        else:
            classCSSStr = ""
        minwidth = ""
        if len(self.nominwidth)>0:
            minwidth="minwidth"
        popupmenuCss=""
        popupmenuTag = ""
        if len(self.popupmenu) > 0:
            popupmenuCss = ' style="display: inline-block;" '
            popupmenuTag = """<i class="fas fa-angle-down" style="padding-left: 5px;float: right;padding-top: 4px"></i>"""
        self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {eventsStr} tabindex="0" {classCSSStr} style="{" ".join(self.style)}" {self.data} >{self.icon}<div class="btn_caption btn_center {minwidth}" {popupmenuCss}>{self.caption}{self.text}</div>{popupmenuTag}""")
        self.SetSysInfo.append("<scriptfile>Components/Button/js/Button.js</scriptfile>")
        self.SetSysInfo.append("<cssfile>Components/Button/css/Button.css</cssfile>")


