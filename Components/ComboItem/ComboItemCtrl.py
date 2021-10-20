from Components.Base.BaseCtrl import *


class ComboItem(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Label';
        self.tag = 'tr';
        self.parentName = ""
        if not self.parentElement.attrib.get("name") == None:
            self.parentName = self.parentElement.attrib.get("name")

        if not "selected" in self.attrs:
            self.selected = ""
        else:
            self.selected = " checked='checked' "
            del self.attrs["selected"]
        if not "checked" in self.attrs:
            self.checked = ""
        else:
            self.checked = " checked='checked' "
            del self.attrs["checked"]


    def ShowMulti(self):
        showtext = ""
        if self.num_element == 1:
            showtext = f"""
                <tr cmptype=\"ComboItem\" isD3Repeater=\"true\">
                    <td>
                        <input type=\"checkbox\" 
                               cont=\"allstate\"
                               onclick=\"D3Api.ComboBoxCtrl.setStateAll(D3Api.getControlByDom(this,'ComboBox'),{self.checked})\"
                        />
                        <span class=\"btnOC\" comboboxname=\"{self.parentName}\"></span>
                        <span>Все</span>
                    </td>
                </tr>
            """
        inp = f'<input type="checkbox" cmpparse="ComboItem" cont="multicheck" {self.selected} onclick="D3Api.ComboItemCtrl.checkItem(this);"/>&nbsp;';
        self.selected = False
        return showtext, inp

    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        inp = ''
        showtext = ''
        if not self.parentElement.attrib.get("multiselect") == None:
            if self.num_element == 1:
                self.print(f"""
                <tr cmptype=\"ComboItem\" isd3repeaterSkip="true">
                    <td>
                        <input type=\"checkbox\" 
                               cont=\"allstate\"
                               onclick=\"D3Api.ComboBoxCtrl.setStateAll(D3Api.getControlByDom(this,'ComboBox'),this.checked)\"
                        />
                        <span class=\"btnOC\" comboboxname=\"{self.parentName}\"></span>
                        <span>Все</span>
                    </td>
                </tr>
                """)
            self.print(f"""
                <tr cmptype="ComboItem" isd3repeater="true" id="d3ctrl{self.genName()}" name="{self.name}" value="{self.value}" comboboxname="{self.parentName}" >
                    <td>
                        <input type="checkbox" cmpparse="ComboItem" cont="multicheck" cont="allstate" onclick="D3Api.ComboItemCtrl.checkItem(this)">
                        <span class="btnOC" comboboxname="{self.parentName}"></span>
                        <span>{self.caption}</span>
                    </td>
                </tr>
            """)
        else:
            self.print(f"""
               <tr cmptype="ComboItem" name="{self.name}" comboboxname="{self.parentName}" value="{self.value}" id="d3ctrl{self.genName()}">
                    <td>
                        <div class="item_block">
                            <span cont="itemcaption">{self.caption}</span>
                        </div>
                    </td>
        """)
        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/ComboBox/js/ComboBox.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/ComboBox/css/ComboBox.css</cssfile>")
