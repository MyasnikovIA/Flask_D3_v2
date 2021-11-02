<div  cmptype="Base" name="94f7af283b8b11eca5020242ac110002" caption=""  width="60%"  height="60%"    formName="Tutorial/Dependences/Dependences" >

    



    <textarea cmptype=Script name="main_script" style="display:none;">
        
            Form.onCreate = function() {
            }
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
        
    </textarea>
    <div  cmptype="Edit" name="RANGE_BEGIN"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"   mask_template="9999999999"  mask_original="0000000000"  emptyMask="true"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <div  cmptype="Edit" name="RANGE_END"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"   mask_template="9999999999"  mask_original="0000000000"  emptyMask="true"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <div  cmptype="Button" name="ButtonOk" onclick="Form.MySendPHP();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Запуск</div></div>

    <div  cmptype="Mask" name="950465c43b8b11eca5020242ac110002"  controls = "RANGE_BEGIN;RANGE_END"   style="display:none" ></div>
    <div  cmptype="Dependences" name="9508a9223b8b11eca5020242ac110002" depend = "ButtonOk"  required = "RANGE_BEGIN;RANGE_END"   style="display:none" ></div>
    



</div>
<div cmptype="sysinfo" style="display:none;"></div>