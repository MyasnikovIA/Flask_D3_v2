from Components.Base.BaseCtrl import *

class LayoutSplit(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Layout';

        if "orientation" in self.attrs:
            self.orientation = self.attrs.get("orientation" )
        else:
            self.orientation = 'vertical';

        if self.orientation == "vertical":
            self.tag = 'td';
        if self.orientation == "horizon":
            self.tag = 'tr';

    def show(self):

        if self.orientation == "horizon":
               self.print(""" <tr style="display: table-row;  border-color: inherit; cursor:s-resize;">
                                <td class="WinLayoutTop" name="s_top" colspan="25" onmousedown="D3Api.LayoutSplitCtrl.mouseDownVert(event)"/>
                              </tr>
                """)
        if self.orientation == "vertical":
            self.print(""" <td class="WinLayoutLeft" name="e_middle" style="cursor:e-resize;"  onmousedown="D3Api.LayoutSplitCtrl.mouseDownHor(event)"/> """)


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