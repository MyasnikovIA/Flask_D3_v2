from Components.Base.BaseCtrl import *

class PageControl(Base):
    """
    необходимо дописать этот компонент
    внутри этого класса обрабатываюстя  вложенные фрагменты <cmpTabSheet />
    """
    def __init__(self, attrs):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'PageControl'
        self.tag = 'div'
        self.mode ="horizontal"
        if "mode" in attrs:
            self.mode = attrs["mode"]
            del attrs["mode"]
        self.text = ""
        if "text" in attrs:
            self.text = attrs["text"]
            del attrs["text"]
        self.printPageArray = []
        self.uniqid = self.genName()
        self.headHtml=[]
        self.bodyHtml = []
        if self.mode == "horizontal":
            self.tagCls ="</div>"
            ind = -1
            for element in self.nodeXML.findall('cmpTabSheet'):
                ind = ind + 1
                caption = ""
                if element.attrib.get("caption"):
                    caption = element.attrib.get("caption")
                active = ""
                if element.attrib.get("active"):
                    active = element.attrib.get("active")
                self.headHtml.append(f"""<li class="ctrl_pageControlTabBtn tab{ind}_{self.uniqid} {active}" pageindex="{ind}" cmptype="TabSheet" name="cmp{self.genName()}" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl{self.genName()}"><a class="centerTB" cont="tabcaption">{caption}</a></li>""")
                self.bodyHtml.append(f""" <div cont="page{ind}_{self.uniqid}" class="ctrl_pageControlTabPage page{ind}_{self.uniqid} " style="display: block;">""")
                sysinfoBlocktmp, htmlContent = parseFrm(element, "", {}, 0)
                self.bodyHtml.append(htmlContent)
                self.bodyHtml.append("</div>")
                self.SetSysInfo.extend(sysinfoBlocktmp)

        if self.mode == "vertical":
            self.tagCls = f"""</div></div>"""
            ind = -1
            for element in self.nodeXML.findall('cmpTabSheet'):
                ind = ind + 1
                caption = ""
                if element.attrib.get("caption"):
                    caption = element.attrib.get("caption")
                active = ""
                if element.attrib.get("active"):
                    active = element.attrib.get("active")
                self.headHtml.append(f""" <li class="ctrl_pageControlTabBtn tab{ind}_{self.uniqid}  {active}" pageindex="{ind}" cmptype="TabSheet" name="tabColumn3" cmptype="TabSheet" title="" onclick="D3Api.PageControlCtrl.showTab(this);">  """)
                self.headHtml.append(f"""   <a class="centerTB" cont="tabcaption">{caption}</a>  """)
                self.headHtml.append(f""" </li> """)
                sysinfoBlocktmp, htmlContent = parseFrm(element, self.formName, {}, 0)
                self.bodyHtml.append(f""" <div cont="page{ind}_{self.uniqid}" class="ctrl_pageControlTabPage page{ind}_{self.uniqid} ">""")
                self.bodyHtml.append(htmlContent)
                self.bodyHtml.append(f""" </div>""")
                self.SetSysInfo.extend(sysinfoBlocktmp)


    def show(self):

        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")

        if self.mode == "horizontal":
            self.print(f"""
<div cmptype="PageControl" name="{self.name}" title="" tabindex="0" class="ctrl_pageControl bg box-sizing-force"  uniqid="{self.uniqid}" mode="{self.mode}" id="d3ctrl{self.genName()}" {eventsStr} {atr}>
    <div cont="div_ul" class="div_ul box-sizing-force">
        <ul cont="PageControl_head" class="ctrl_pageControlTabs bg" style="left: 0px;">
            {" ".join(self.headHtml)}
        </ul>
        <div cont="ScrollNext" class="button_scroll next_scroll" onclick="D3Api.PageControlCtrl.ScrollNext(this);" style="display: none;"></div>
        <div cont="ScrollPrior" class="button_scroll prior_scroll" onclick="D3Api.PageControlCtrl.ScrollPrior(this);" style="display: none;"></div>
    </div>
     {" ".join(self.bodyHtml)}
</div>
""")
        if self.mode == "vertical":
            self.print(f"""
<div  name="{self.name}"  cmptype="PageControl" title="" tabindex="0" class="ctrl_pageControl bg box-sizing-force" uniqid="{self.uniqid}" mode="vertical" {eventsStr} {atr}>
    <div cont="div_ul" class="div_ul box-sizing-force">
        <ul cont="PageControl_head" class="ctrl_pageControlTabs bg">
          {" ".join(self.headHtml)}
        </ul>
    </div>
    <div class="pageControl-content">
 {" ".join(self.bodyHtml)}
""")

        # self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>\n{self.text}""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/PageControl/js/PageControl.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/PageControl/css/PageControl.css</cssfile>")

        # очистка содержимого блока
        for element in self.nodeXML.findall('*'):
            self.nodeXML.remove(element)
