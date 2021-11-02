<div  cmptype="Base" name="3a0a6e6e3b8d11ec8c080242ac110002" class="Main ActiveDashBoard box-sizing-force"  caption="Тестовое окно"  oncreate="Form.onCreate()"  formName="Tutorial/Layout/layout" >

    <textarea cmptype=Script name="MainScript" style="display:none;">
       
            Form.onCreate = function() {
                setVar("form_params22","12345");
                setVar("paramArrDS",{"testparam1":123,"testParam2":345});
                console.log("1111111111");
            }
       
    </textarea>

    <div  cmptype="Button" name="3a0abd743b8d11ec8c080242ac110002" onclick="Form.openD3Form();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Form.openD3Form</div></div>
    <div  cmptype="Button" name="3a0afd8e3b8d11ec8c080242ac110002" onclick="Form.getLay();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Form.MyLayout</div></div>

     <table class="WinLayout" cmptype="Layout" name="MyLayout"   style="height:100%; width:100% ; ext-indent: initial; border-spacing: 2px; background-color: rgb(210, 210, 210); height:90%"   text="

        "> 

        <td class="WinLayout" cmptype="LayoutContainer" name="3a10b3aa3b8d11ec8c080242ac110002"   style="vertical-align: top; background-size: 100% 100%; height:125px"  colspan="22"  text="
              "  >
              
                <span  cmptype="Label" name="3a1436b03b8d11ec8c080242ac110002"  class='label'    > Верхняя панель </span>
        </td>

        
         <tr name="3a17cb403b8d11ec8c080242ac110002"   cmptype="Layoutsplit" name="3a17cb403b8d11ec8c080242ac110002"  style="display: table-row;  border-color: inherit; cursor:s-resize;">
                                <td class="WinLayoutTop" name="s_top" colspan="25" onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'top')"/>
                              </tr>
                </tr>

             
             <td class="WinLayout" cmptype="LayoutContainer" name="3a1b24523b8d11ec8c080242ac110002"   style="vertical-align: top; background-size: 100% 100%;"  text="
                "  >
                
                <span  cmptype="Label" name="3a1b4c5c3b8d11ec8c080242ac110002"  class='label'    > Левая панель  </span>
            </td>

            
             <td class="WinLayoutLeft" cmptype="Layoutsplit" name="3a1b73763b8d11ec8c080242ac110002"  style="cursor:e-resize;"  onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'left')"/> </td>


            <td class="WinLayout" cmptype="LayoutContainer" name="3a1b9b763b8d11ec8c080242ac110002"   style="vertical-align: top; background-size: 100% 100%;"  text="
                "  >
                
                <span  cmptype="Label" name="3a1bc9ac3b8d11ec8c080242ac110002"  class='label'    > Центральная панель </span>
                <div  cmptype="Edit" name="test3"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"     disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
                <div  cmptype="Edit" name="test3"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"     disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
            </td>

            
             <td class="WinLayoutLeft" cmptype="Layoutsplit" name="3a1c4ada3b8d11ec8c080242ac110002"  style="cursor:e-resize;"  onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'left')"/> </td>

            
            <td class="WinLayout" cmptype="LayoutContainer" name="3a1c730c3b8d11ec8c080242ac110002"   style="vertical-align: top; background-size: 100% 100%;"    ><div  cmptype="Base" name="MAINFORM" width="60%"  height="60%"  caption="Примеры использования контролов"    formName="Tutorial/main" >

     <div  cmptype="Button" name="3a1d9c003b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Expander/expander',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Expander component</div></div>
     <div  cmptype="Button" name="3a1dc3a63b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Layout/layout',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Layout component</div></div>
     <div  cmptype="Button" name="3a1dea703b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/ComboBox/ComboBox',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Сombobox component</div></div>
     <div  cmptype="Button" name="3a1e0fd23b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Dependences/Dependences',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Dependences component</div></div>
     <div  cmptype="Button" name="3a1e362e3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Mask/Mask',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Mask component</div></div>
     <div  cmptype="Button" name="3a1e60cc3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/TextArea/TextArea',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >TextArea component</div></div>
     <div  cmptype="Button" name="3a1e88fe3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/PopupMenu/PopupMenu',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >PopupMenu component</div></div>
     <div  cmptype="Button" name="3a1eb23e3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/CheckBox/CheckBox',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >CheckBox component</div></div>
     <div  cmptype="Button" name="3a1edeb23b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Dialog/Dialog',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Dialog component</div></div>
     <div  cmptype="Button" name="3a1f07c03b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/SubForm/SubForm',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >SubForm component</div></div>
     <div  cmptype="Button" name="3a1f69403b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Window/startModalWin',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Window component</div></div>
     <div  cmptype="Button" name="3a1fa1443b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Image/image',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >image component</div></div>
     <div  cmptype="Button" name="3a1fe3de3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Toolbar/Toolbar',true)" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Toolbar component</div></div>
     <div  cmptype="Button" name="3a2010843b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Desktop/Desktop',true,{width: 1200, height: 900})" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Desktop component</div></div>
     <div  cmptype="Button" name="3a203b0e3b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/PageControl/PageControl',true,{width: 1200, height: 900})" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >PageControl horizontal</div></div>
     <div  cmptype="Button" name="3a2069623b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/PageControl/PageControlVert',true,{width: 1200, height: 900})" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >PageControl vertical</div></div>
     <div  cmptype="Button" name="3a2091123b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Tabs/Tabs',true,{width: 1200, height: 900})" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Tabs (аналог PageControl)</div></div>
     <div  cmptype="Button" name="3a20b7503b8d11ec8c080242ac110002" onclick="openD3Form('Tutorial/Tree/Tree',true,{width: 1200, height: 900})" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Tree</div></div>
</div></td>

        
         <tr name="3a20e86a3b8d11ec8c080242ac110002"   cmptype="Layoutsplit" name="3a20e86a3b8d11ec8c080242ac110002"  style="display: table-row;  border-color: inherit; cursor:s-resize;">
                                <td class="WinLayoutTop" name="s_top" colspan="25" onmousedown="D3Api.LayoutSplitCtrl.moveSplit(event,'top')"/>
                              </tr>
                </tr>
        <td class="WinLayout" cmptype="LayoutContainer" name="3a210f8e3b8d11ec8c080242ac110002"   style="vertical-align: top; background-size: 100% 100%;"  colspan="25"  text="
            Нижняя панель
        "  >
            Нижняя панель
        </td>

    </table>

</div>
<div cmptype="sysinfo" style="display:none;"></div>