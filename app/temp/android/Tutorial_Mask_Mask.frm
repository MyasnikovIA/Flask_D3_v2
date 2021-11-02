<div  cmptype="Base" name="2da72fe03b8d11ec9a2e0242ac110002" caption=""  width="60%"  height="60%"    formName="Tutorial/Mask/Mask" >

    <textarea cmptype=Script name="main_script" style="display:none;">
        
            Form.onCreate = function() {
               // Добавить фильтр и маску в коде
               // callControlMethod('Depend', 'removeRequiredControl', 'INC_VAL', true);
               // callControlMethod('Depend', 'removeRequiredControl', 'START_VAL', true);
               // D3Api.MaskCtrl.setParam(getControl('MAX_VAL'), 'mask_type', 'number');
               // D3Api.MaskCtrl.setParam(getControl('MAX_VAL'), 'mask_template_regular', new RegExp(/^\d+$/));
            }
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
        
    </textarea>
    <br/>Ввести число <div  cmptype="Edit" name="RANGE_BEGIN"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"   mask_template="9999999999"  mask_original="0000000000"  emptyMask="true"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <br/>Ввести время<div  cmptype="Edit" name="ACCEPT_TIME"   class='ctrl_edit editControl box-sizing-force' style = "width: 20%;"   mask_template="99:99"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <br/>Ввести дату и время DD:HH:MI:SS<div  cmptype="Edit" name="L_COSTS"   class='ctrl_edit editControl box-sizing-force' style = "width: 20%;"  placeholder = "DD:HH:MI:SS"   mask_template="99:99:99:99"  mask_original="00:00:00:00"  mask_check_regular="^([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])$"  mask_template_regular="^([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])$"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "  placeholder = "DD:HH:MI:SS"   /></div>


    <br/>Ввести телефон<div  cmptype="Edit" name="PHONE"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"  placeholder = "+7(NNN)NNN-NN-NN"   data="value:CREATE_EMP_PHONE;"  mask_original="+7(000)0000000"  mask_template="+7(999)9999999"  emptyMask="false"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "  placeholder = "+7(NNN)NNN-NN-NN"   /></div>
    <br/>Ввести СНИЛС<div  cmptype="Edit" name="CC_SNILS"   class='ctrl_edit editControl box-sizing-force' style = "width: 100px;"   mask_template_regular="^[0-9]{3}-[0-9]{3}-[0-9]{3}\s{1}[0-9]{2}$"  mask_check_regular="^[0-9]{3}-[0-9]{3}-[0-9]{3}\s{1}[0-9]{2}$"  mask_empty="true"  mask_original="000-000-000 00"  mask_template="999-999-999 99"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <br/>Ввести TOKEN <div  cmptype="Edit" name="ctrlTOKEN"   class='ctrl_edit editControl box-sizing-force' style = "width: 50%;"  placeholder = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"   mask_template_regular="^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"  mask_check_regular="^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"  help="Укажите токен ключ"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "  placeholder = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"   /></div>

    <div  cmptype="Button" name="ButtonOk" onclick="Form.MySendPHP();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Запуск</div></div>

    <div  cmptype="Mask" name="2da8f7583b8d11ec9a2e0242ac110002"  controls = "RANGE_BEGIN;RANGE_END;ACCEPT_TIME;CC_SNILS;L_COSTS;ctrlTOKEN;PHONE"   style="display:none" ></div>
    <div  cmptype="Dependences" name="2da926743b8d11ec9a2e0242ac110002" depend = "ButtonOk"  required = "RANGE_BEGIN;RANGE_END"   style="display:none" ></div>
</div>
<div cmptype="sysinfo" style="display:none;"></div>