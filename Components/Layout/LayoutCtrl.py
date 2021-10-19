from Components.Base.BaseCtrl import *

class Layout(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Layout';
        self.tag = 'table';
        if "style" in self.attrs:
            self.style = f""" style="height:100%; width:100% ; ext-indent: initial; border-spacing: 2px; background-color: rgb(210, 210, 210); {self.attrs.get("style")}" """
            del self.attrs["style"]
        else:
            self.style = """ style="height:100%; width:100% ; ext-indent: initial; border-spacing: 2px; background-color: rgb(210, 210, 210);" """

    def show(self):
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        self.print(f""" <table class=" WinLayout"  cmptype="{self.CmpType}" name="{self.name}"  {self.style} {eventsStr} {atr}> """)
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Layout/js/Layout.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Layout/css/Layout.css</cssfile>")

"""

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