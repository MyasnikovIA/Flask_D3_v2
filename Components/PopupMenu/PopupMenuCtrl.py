from Components.Base.BaseCtrl import *


class PopupMenu(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'PopupItem';
        self.tag = 'div';
        self.isJoin = ArrKeyRtrn(self.attrs, 'join_menu', False);
        self.joinGroup = ArrKeyRtrn(self.attrs, 'join_group', False);
        self.lastitem = None;
        self.text = '';
        self.text = ""
        self.styleArr = ["z-index: 10", "left: 136px", "top: 9px"]
        if 'style'in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        if 'text' in self.attrs:
            del self.attrs['text']


    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""
<div class="popupMenu"  name="{self.name}"  cmptype="PopupMenu" title="" tabindex="0" cont="menu" id="d3ctrl{self.genName()}" {atr} {eventsStr} style="{';'.join(self.styleArr)}">
    <div class="item waittext">Подождите...</div>
""")

        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/Edit/js/Edit.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Edit/css/Edit.css</cssfile>")


"""




<div class="popupMenu" name="pMENU" cmptype="PopupMenu" title="" tabindex="0" cont="menu" id="d3ctrl131635341869511"
     style="z-index: 10; left: 136px; top: 9px;">
    <div class="item waittext">Подождите...</div>
  
    <div class="item active" cmptype="PopupItem" name="cmp6179562f0ce9b" title="" rootitem="true"
         caption="22222222222222222" id="d3ctrl161635341869511">
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick="alert(1)D3Api.PopupItemCtrl.clickItem(this);" onmouseover="D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption"><img src="" cont="itemIcon" class="itemIcon"><span cont="itemCaption">22222222222222222</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
    </div>
    
    <div class="item " cmptype="PopupItem" name="cmp6179562f0d6b3" title="" rootitem="true" caption="11111111111111111"  id="d3ctrl191635341869511">
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick="alert(1)D3Api.PopupItemCtrl.clickItem(this);" onmouseover="D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption">
                    <img src="" cont="itemIcon" class="itemIcon"><span cont="itemCaption">11111111111111111</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
    </div>
    
</div>



<div class="item separator ctrl_hidden" item_split="true" cmptype="PopupItem" id="d3ctrl691635342474373"></div>


<body style="height: 100%;" onresize="D3Api.resize(false);" oncontextmenu="return D3Api.onContextMenuBody(event);" onbeforeunload1="return 'Внимание.';">
 
 
<div class="popupMenu" name="pMENU" cmptype="PopupMenu" title="" tabindex="0" cont="menu" id="d3ctrl131635341690363"
     style="z-index: 10; display: block; left: 118px; top: 7px;">
    <div class="item waittext">Подождите...</div>
    <div class="item active" cmptype="PopupItem" name="cmp6179557bdddc6" title="" rootitem="true" caption="1" id="d3ctrl161635341690363">
        
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick="alert(1)D3Api.PopupItemCtrl.clickItem(this);" onmouseover="D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption"><img src="" cont="itemIcon" class="itemIcon"><span cont="itemCaption">1</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
        
    </div>
    <div class="popupGroupItem" cont="groupitem" name="additionalMainMenu" cmptype="PopupGroupItem" id="d3ctrl191635341690363"></div>
    <div class="item separator ctrl_hidden" item_split="true" cmptype="PopupItem" id="d3ctrl331635341690366"></div>
    <div class="popupGroupItem" cont="groupitem" name="system" cmptype="PopupGroupItem" separator="before" id="d3ctrl221635341690363"></div>
</div>





<div class="popupMenu" name="pMENU" cmptype="PopupMenu" title="" tabindex="0" cont="menu" id="d3ctrl131635341869511"
     style="z-index: 10; display: block; left: 136px; top: 9px;">
    <div class="item waittext">Подождите...</div>
    
    <div class="item active" cmptype="PopupItem" name="cmp6179562f0ce9b" title="" rootitem="true"
         caption="22222222222222222" id="d3ctrl161635341869511">
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick="alert(1)D3Api.PopupItemCtrl.clickItem(this);" onmouseover="D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption"><img src="" cont="itemIcon" class="itemIcon"><span cont="itemCaption">22222222222222222</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
    </div>
    
    <div class="item " cmptype="PopupItem" name="cmp6179562f0d6b3" title="" rootitem="true" caption="11111111111111111"
         id="d3ctrl191635341869511">
        <table style="width:100%" cmpparse="PopupItem" cont="item"
               onclick="alert(1)D3Api.PopupItemCtrl.clickItem(this);"
               onmouseover="D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption"><img src="" cont="itemIcon" class="itemIcon"><span cont="itemCaption">11111111111111111</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
    </div>
    
    <div class="popupGroupItem" cont="groupitem" name="additionalMainMenu" cmptype="PopupGroupItem" id="d3ctrl221635341869511"></div>
    <div class="item separator ctrl_hidden" item_split="true" cmptype="PopupItem" id="d3ctrl361635341869513"></div>
    <div class="popupGroupItem" cont="groupitem" name="system" cmptype="PopupGroupItem" separator="before" id="d3ctrl251635341869511"></div>
</div>
"""