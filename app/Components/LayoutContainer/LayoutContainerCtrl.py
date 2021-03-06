from Components.Base.BaseCtrl import *


class LayoutContainer(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'LayoutContainer';
        self.tag = 'td';
        if "style" in self.attrs:
            self.style = f""" style="vertical-align: top; background-size: 100% 100%; {self.attrs.get("style")}" """
            del self.attrs["style"]
        else:
            self.style = """ style="vertical-align: top; background-size: 100% 100%;" """
        self.path = ""
        if 'path' in self.attrs:
            self.path = self.attrs["path"]
            del self.attrs['path']

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        if len(self.path) == 0 :
            self.print(f"""<td class="WinLayout" cmptype="{self.CmpType}" name="{self.name}"  {self.style} {atr} {eventsStr} >""")
        else:
            rootForm = getXMLObject(self.path)
            sysinfoBlock, htmlContent = parseFrm(rootForm, self.path, {}, 0)  # парсим форму
            self.print( f"""<td class="WinLayout" cmptype="{self.CmpType}" name="{self.name}"  {self.style} {atr} {eventsStr} >{htmlContent}""")
            self.SetSysInfo.extend(sysinfoBlock)
        # Добавляется при инициализации  d3main.js d3theme.css
        # self.SetSysInfo.append("<scriptfile>Components/LayoutContainer/js/LayoutContainer.js</scriptfile>")
        # self.SetSysInfo.append("<cssfile>Components/LayoutContainer/css/LayoutContainer.css</cssfile>")

"""
cmptype="{self.CmpType}" name="{self.name}"  
    <table class="window WinLayout" name="modal_win" style="height:80%; width:90% ; ext-indent: initial; border-spacing: 2px; background-color: rgb(210, 210, 210);">
        <tbody>

       <!-- верхний контейнер -->
       <tr style="display: table-row; vertical-align: inherit; border-color: inherit;height:20%;">
           <td>sssssssss</td>
       </tr>

       <!-- верхний разделитель -->
       <tr style="display: table-row;  border-color: inherit; cursor:s-resize;">
           <td class="WinLayoutTop" name="s_top" colspan="25"/>
       </tr>


        <tr style="display: table-row; vertical-align: inherit; border-color: inherit;">

            <td class="WinLayout" style="vertical-align: top; background-size: 100% 100%;">
                Right
            </td>

            <!--  левый Сплитер -->
            <td class="WinLayoutLeft" name="e_middle" style="cursor:e-resize;"/>

            <td class="WinLayout" style="vertical-align: top; background-size: 100% 100%;">
                  Content
            </td>

            <!--  правый  Сплитер-->
            <td class="WinLayoutLeft" name="e_middle" style="cursor:e-resize;"/>

            <td class="WinLayout" style="vertical-align: top; background-size: 100% 100%;">
                Content Left
            </td>
        </tr>

            <tr style="display: table-row; vertical-align: inherit; border-color: inherit;height:20%;">
                   <td class="WinLayoutBottom" name="s_bottom" colspan="25"></td>
                Bottom
            </tr>

        </tbody>
    </table>

"""
