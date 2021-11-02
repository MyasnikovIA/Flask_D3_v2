<div  cmptype="Base" name="a00b8d803b8b11eca9de0242ac110002" caption=""  width="60%"  height="60%"    formName="Tutorial/Dialog/Dialog" >

    <textarea cmptype=Script name="a00bbb663b8b11eca9de0242ac110002" style="display:none;">
        
            Form.onBtnTest2 = function() {
              setVisible('d_wg_delete_Ctrl', true);
            }
            Form.onBtnTest3 = function() {
              var win3 = new DConfirmWindow("Вы уверены...?", function(){ console.log('вы нажали OK');}, function(){ console.log('вы нажали отмена');} );
              win3.show();
            }
        
    </textarea>
   <div  cmptype="Button" name="a00be7bc3b8b11eca9de0242ac110002" onclick="Form.onBtnTest3();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Error</div></div>
   <div  cmptype="Button" name="a00c1a203b8b11eca9de0242ac110002" onclick="Form.onBtnTest2();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >ffasdfgsd</div></div>

    <h1>Дописать пример!!!</h1>
    <div name="d_wg_delete_Ctrl" cmptype="Dialog"/>
        
    <h1>Дописать пример!!!</h1>
</div>
<div cmptype="sysinfo" style="display:none;"></div>