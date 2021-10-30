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
        self.text = ""
        if "text" in attrs:
            self.text = attrs["text"]
            del attrs["text"]
        self.printPageArray = []
        self.uniqid = self.genName()
        if self.mode == "horizontal":
            self.tagCls ="</div>"
        if self.mode == "vertical":
            self.tagCls ="</div>"


    def show(self):

        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")

        if self.mode == "horizontal":
            self.print(f""" """)
        if self.mode == "vertical":
            self.print(f""" """)

        # self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>\n{self.text}""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/TabSheet/js/TabSheet.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/TabSheet/css/TabSheet.css</cssfile>")

        # очистка содержимого блока
        for element in self.nodeXML.findall('*'):
            self.nodeXML.remove(element)

"""

<div cmptype="PageControl" name="cmp617c7ebf2ce7f" title="" tabindex="0" class="ctrl_pageControl bg box-sizing-force"  uniqid="pc617c7ebf2ceb6" mode="horizontal" id="d3ctrl101635548858541">
    <div cont="div_ul" class="div_ul box-sizing-force">
        <ul cont="PageControl_head" class="ctrl_pageControlTabs bg" style="left: 0px;">
            <li class="ctrl_pageControlTabBtn tab0_pc617c7ebf2ceb6 active" pageindex="0" cmptype="TabSheet" name="cmp617c7ebf2dbaf" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl131635548858541"><a class="centerTB" cont="tabcaption">1111111111</a></li>
            <li class="ctrl_pageControlTabBtn tab1_pc617c7ebf2ceb6  " pageindex="1" cmptype="TabSheet" name="cmp617c7ebf2e608" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl161635548858541"><a class="centerTB" cont="tabcaption">22222222</a></li>
        </ul>
        <div cont="ScrollNext" class="button_scroll next_scroll" onclick="D3Api.PageControlCtrl.ScrollNext(this);" style="display: none;"></div>
        <div cont="ScrollPrior" class="button_scroll prior_scroll" onclick="D3Api.PageControlCtrl.ScrollPrior(this);" style="display: none;"></div>
    </div>

    <div cont="page0_pc617c7ebf2ceb6" class="ctrl_pageControlTabPage page0_pc617c7ebf2ceb6 " style="display: block;">
        содержимое1111
    </div>
    <div cont="page1_pc617c7ebf2ceb6" class="ctrl_pageControlTabPage page1_pc617c7ebf2ceb6 ">
        содержимое2222
    </div>
</div>
      
      
      
<div cmptype="Form" scrollable="true" formname="main" id="d3ctrl31635549033391" class="" style="margin-top: 0px; height: 100%;">
    <div>
        <div cmptype="Base" tabindex="0" name="firstControl" oncreate="D3Api.BaseCtrl.init_focus(this);" id="d3ctrl61635549033392"></div>
    </div>
    <textarea cmptype="Script" name="cmp617c7f6e05195" style="display:none;">
            Form.onBtnTest2 = function() {
              setVisible('d_wg_delete_Ctrl', true);
            }
    </textarea>


    <div cmptype="PageControl" name="cmp617c7f6e0881c" title="" tabindex="0" class="ctrl_pageControl bg box-sizing-force" uniqid="pc617c7f6e08854" mode="vertical" id="d3ctrl101635549033392">
        <div cont="div_ul" class="div_ul box-sizing-force">
            <ul cont="PageControl_head" class="ctrl_pageControlTabs bg">
                <li class="ctrl_pageControlTabBtn tab0_pc617c7f6e08854 active" pageindex="0" cmptype="TabSheet" name="cmp617c7f6e096e8" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl131635549033392"><a class="centerTB" cont="tabcaption">1111111111</a></li>
                <li class="ctrl_pageControlTabBtn tab1_pc617c7f6e08854" pageindex="1" cmptype="TabSheet" name="cmp617c7f6e09ff0" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl161635549033392"><a class="centerTB" cont="tabcaption">22222222</a></li>
            </ul>
        </div>
        <div class="pageControl-content">
            <div cont="page0_pc617c7f6e08854" class="ctrl_pageControlTabPage page0_pc617c7f6e08854 " style="display: block;">
                содержимое1111
            </div>
            <div cont="page1_pc617c7f6e08854" class="ctrl_pageControlTabPage page1_pc617c7f6e08854 " style="display: none;">
                содержимое2222
            </div>
        </div>
    </div>


    <div>
        <div cmptype="Base" tabindex="0" name="lastControl" oncreate="D3Api.BaseCtrl.init_focus(this);" id="d3ctrl191635549033392"></div>
    </div>
</div>
      
"""