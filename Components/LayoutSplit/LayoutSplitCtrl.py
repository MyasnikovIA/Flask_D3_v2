from Components.Base.BaseCtrl import *

class LayoutSplit(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Layoutsplit';

        if "orientation" in self.attrs:
            self.orientation = self.attrs.get("orientation" )
            del self.attrs["orientation"]
        else:
            self.orientation = 'vertical';


        if self.orientation == "vertical":
            self.tag = 'td';

        if self.orientation == "horizon":
            self.tag = 'tr';

        # Установка направление в котором будет изменятся блок
        if "direction" in self.attrs:
            self.direction = self.attrs.get("direction" )
            del self.attrs["direction"]
        else:
            if self.orientation == "vertical":
                self.direction = 'left';
            else:
                self.direction = 'top';


    def show(self):
        if self.orientation == "horizon":
               self.print(f""" <tr name="{self.name}"   cmptype="{self.CmpType}" name="{self.name}"  style="display: table-row;  border-color: inherit; cursor:s-resize;">
                                <td class="WinLayoutTop" name="s_top" colspan="25" onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'{self.direction}')"/>
                              </tr>
                """)
        if self.orientation == "vertical":
            self.print(f""" <td class="WinLayoutLeft" cmptype="{self.CmpType}" name="{self.name}" name="{self.name}"  style="cursor:e-resize;"  onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'{self.direction}')"/> """)

        #if self.orientation == "horizon":
        #       self.print(f""" <tr  cmptype="{self.CmpType}" name="{self.name}"   style="display: table-row;  border-color: inherit; cursor:s-resize;">
        #                        <td class="WinLayoutTop" name="s_top" colspan="25" onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'{self.direction}')"/>
        #                      </tr>
        #        """)
        #if self.orientation == "vertical":
        #    self.print(f""" <td class="WinLayoutLeft" cmptype="{self.CmpType}" name="{self.name}"  style="cursor:e-resize;"  onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'{self.direction}')"/> """)


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