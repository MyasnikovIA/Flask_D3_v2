from Components.Base.BaseCtrl import *


class Edit(Base):
    """
         <table  cmptype="Edit" name='testEd'  title='' class="editControl" cellspacing="0" cellpadding="0" style="vertical-align:bottom; width:114px;  display:inline-table;" >
              <tr>
                  <td class="td_edit_control">
                      <input type="text" cmpparse="Edit" value=""   class="input-ctrl"/>
                  </td>
              </tr>
         </table>
    """

    def __init__(self, attrs):
        super().__init__(attrs)
        self.readonly = getBooleanAttr('readonly', self.attrs, 'false');

        if 'class' not in self.attrs:
            self.classCSS = ['ctrl_edit', 'editControl', 'box-sizing-force']
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']
        if ('ctrl_edit' not in self.classCSS):
            self.classCSS.append('ctrl_edit')
        if ('editControl' not in self.classCSS):
            self.classCSS.append('editControl')
        if ('box-sizing-force' not in self.classCSS):
            self.classCSS.append('box-sizing-force')
        self.CmpType = 'Edit';
        self.tag = 'div';
        self.placeholder = getDomAttrRemove('placeholder', None, self.attrs);
        self.maxlength = getDomAttrRemove('maxlength', None, self.attrs);
        self.value = getDomAttrRemove('value', None, self.attrs);
        self.type = getDomAttrRemove('type', 'text', self.attrs);
        self.format = getDomAttrRemove('format', None, self.attrs);
        self.readonly = getDomAttrRemove('readonly', None, self.attrs);
        self.disabled = getDomAttrRemove('disabled', None, self.attrs);
        self.format = RemoveArrKeyRtrn(self.attrs, 'format', '');

        if not "width" in self.attrs:
            width = "100%"
        else:
            width = self.attrs["width"]
            del self.attrs["width"]
        if not "style" in self.attrs:
            self.style = f'style = "width: {width};"'
        else:
            self.style = f""" style = "width: {width};{self.attrs["style"]}" """
            del self.attrs["style"]

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        if len(self.classCSS) > 0:
            classCSSStr = f""" class='{' '.join(self.classCSS)}'"""
        else:
            classCSSStr = ""
        self.print(
            f"""<div  cmptype="{self.CmpType}" name="{self.name}"  {classCSSStr} {self.style} {self.placeholder}  {atr}  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"  {self.type} {self.value} {self.maxlength} {self.readonly} {eventsStr}  onchange="D3Api.stopEvent(); " {self.placeholder} {self.disabled} />""")
        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/Edit/js/Edit.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/Edit/css/Edit.css</cssfile>")
