
from Components.Base.BaseCtrl import *


class CheckBox(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'CheckBox';
        self.tag = 'tr';
        self.parentName = ""
        if 'class' not in self.attrs:
            self.classCSS = []
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']

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

        if not "valuechecked" in self.attrs:
            self.valuechecked = ""
        else:
            self.valuechecked = f' valuechecked="{self.attrs["valuechecked"]}" '
            del self.attrs["valuechecked"]

        if not "valueunchecked" in self.attrs:
            self.valueunchecked = ""
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
        styleTxt = f' style="{self.style}" '

        if len(self.disabled)>0:
            self.disabled = " disabled=\"disabled\" "

        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        inp = ''
        showtext = ''
        if not self.parentElement.attrib.get("multiselect") == None:
            if self.num_element == 1:
                self.print(f""" <div cmptype="{self.CmpType}" {atr} {classCSSStr} {eventsStr} {styleTxt}><label><input type="checkbox" {self.disabled } {self.checked}{self.readonly} /><span>{self.caption}</span></label></div>""")

#'';