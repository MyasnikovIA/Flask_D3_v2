
from Components.Base.BaseCtrl import *


class CheckBox(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'CheckBox';
        self.tag = 'tr';
        self.parentName = ""

        self.styleArr=[]
        if 'style'in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']

        if 'class' not in self.attrs:
            self.classCSS = []
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']

        self.caption = ""
        if 'caption' in self.attrs:
            self.caption =self.attrs["caption"]
            del self.attrs['caption']

        self.onclick = ""
        if 'onclick' in self.attrs:
            self.onclick =  f' onclick="{self.attrs["onclick"]}" '
            del self.attrs['onclick']
        self.onchange = ""
        if 'onchange' in self.attrs:
            self.onchange =  f' onchange="{self.attrs["onchange"]}" '
            del self.attrs['onchange']

        if not self.parentElement.attrib.get("name") == None:
            self.parentName = self.parentElement.attrib.get("name")
        if not "checked" in self.attrs:
            self.checked = ""
        else:
            self.checked = " checked='checked' "
            del self.attrs["checked"]
        if not "readonly" in self.attrs:
            self.readonly = ""
        else:
            self.readonly = " readonly='readonly' "
            del self.attrs["readonly"]

        if not "disabled" in self.attrs:
            self.disabled = ""
        else:
            self.disabled = ' disabled="disabled" '
            del self.attrs["disabled"]

        if not "valuechecked" in self.attrs:
            self.valuechecked = ' valuechecked="1" '
        else:
            self.valuechecked = f' valuechecked="{self.attrs["valuechecked"]}" '
            del self.attrs["valuechecked"]

        if not "valueunchecked" in self.attrs:
            self.valueunchecked = ' valueunchecked="0" '
        else:
            if self.value == self.attrs["valueunchecked"]:
                self.checked = " checked='checked' "
            else:
                self.checked = ""
            self.valueunchecked = f' valueunchecked="{self.attrs["valueunchecked"]}" '
            del self.attrs["valueunchecked"]

    def show(self):
        if len(self.classCSS) > 0:
            classCSSStr = f""" class='{' '.join(self.classCSS)}'"""
        else:
            classCSSStr = ""
        styleTxt = f' style="{";".join(self.styleArr)}" '

        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<div name="{self.name}" cmptype="CheckBox" title="" {self.valuechecked} {self.valueunchecked} {classCSSStr} id="d3ctrl{self.genName()}" {atr}{eventsStr}{styleTxt}><label><input type="checkbox"  {self.checked}{self.readonly}{self.disabled} {self.onclick}{self.onchange}><span>{self.caption}</span></label></div>""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/CheckBox/js/CheckBox.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/CheckBox/css/CheckBox.css</cssfile>")




        #if len(self.disabled)>0:
        #    self.disabled = " disabled=\"disabled\" "
        #eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        #atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        #inp = ''
        #showtext = ''
        #if not self.parentElement.attrib.get("multiselect") == None:
        #    if self.num_element == 1:
        #        self.print(f""" <div cmptype="{self.CmpType}" {atr} {classCSSStr} {eventsStr} {styleTxt}><label><input type="checkbox" {self.disabled } {self.checked}{self.readonly} /><span>{self.caption}</span></label></div>""")

#'';