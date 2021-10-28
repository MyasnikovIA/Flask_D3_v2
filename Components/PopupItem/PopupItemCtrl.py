from Components.Base.BaseCtrl import *


class PopupItem(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'PopupItem';
        if 'text' in  self.attrs:
            self.tagCls = '</div></div><div class="popupGroupItem" cont="groupitem" name="additionalMainMenu" cmptype="PopupGroupItem"></div><div class="popupGroupItem" cont="groupitem" name="system" cmptype="PopupGroupItem" ></div>';
        else:
            self.tagCls = '''</div> <div class="popupGroupItem" cont="groupitem" name="additionalMainMenu" cmptype="PopupGroupItem"></div><div class="popupGroupItem" cont="groupitem" name="system" cmptype="PopupGroupItem" ></div>''';
        self.tag = 'div';

        self.text = ""
        self.onclick = ""
        if 'onclick' in self.attrs:
            self.onclick = self.attrs["onclick"]
            del self.attrs['onclick']
        self.onmouseover = ""
        if 'onmouseover' in self.attrs:
            self.onmouseover = self.attrs["onmouseover"]
            del self.attrs['onmouseover']
        self.caption = ""
        if 'caption' in self.attrs:
            self.caption = self.attrs["caption"]
            del self.attrs['caption']
        self.icon = ""
        self.placeholder = ""
        if 'placeholder' in self.attrs:
            self.placeholder = self.attrs["placeholder"]
            del self.attrs['placeholder']
        self.icon = ""

        #icon = "~CmpPopupMenu/Icons/generation" / >
        #  std_icon="generation"
        if 'icon' in self.attrs:
            if '~Cmp' in self.attrs["icon"]:
                self.icon = f"/Components/PopupMenu/images/Icons/{self.attrs['icon'][4:]}.png"
            else:
                self.icon = self.attrs["icon"]
            del self.attrs['icon']
        if 'std_icon' in self.attrs:
            self.icon = f"/Components/PopupMenu/images/Icons/{self.attrs['std_icon']}.png"
            del self.attrs['std_icon']


    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        subItems=""

        if 'text' in self.attrs: # Если есть ребенок
            subItems = '''<div class="popupMenu subItems" cont="menu" style="left: 171.141px; top: 0px; z-index: 10;">'''
        split = ""
        if self.caption == "-":
           self.print(f"""<div class="item separator " cmptype="PopupItem" name="{self.name}" title="" rootitem="true" item_split="true" id="d3ctrl{self.genName()}" {eventsStr} {atr}>{subItems}""")
        else:
           self.print(f"""
   <div class="item " cmptype="PopupItem" name="{self.name}" title="{self.placeholder}" rootitem="true" {split} caption="{self.caption}"  id="d3ctrl{self.genName()}" {eventsStr} {atr}>
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick="{self.onclick};D3Api.PopupItemCtrl.clickItem(this);" onmouseover="{self.onmouseover};D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption">
                    <img src="{self.icon}" cont="itemIcon" class="itemIcon"><span cont="itemCaption">{self.caption}</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
        {subItems}
""")

        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/PopupMenu/js/PopupMenu.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/PopupMenu/css/PopupMenu.css</cssfile>")
