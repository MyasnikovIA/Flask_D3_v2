<div  cmptype="Base" name="MAINFORM" class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()"  formName="Tutorial/Window/startModalWin" >

    
    <textarea cmptype=Script name="ffffff" style="display:none;">
        
            Form.onCreate = function() {
            }
            Form.selectOkato = function() {
                win = openD3Form('selectValue',true,{left:10,vars:{valueVar: 'ddddddddddddd' },onclose:[closure(Form.setResult)]});
            }
            Form.setResult = function(res) {
                if(res) {
                    alert( res.value );
                }
            }

        
    </textarea>



    <textarea cmptype=Script name="201128ea3b8d11ec9f450242ac110002" style="display:none;">
        Form.selectOkato = function() {
            win = openD3Form('Tutorial/Window/selectValue',true,{left:100,vars:{valueVar: getValue('can_edit') },onclose:[closure(Form.setResult)]});
        }
        Form.setResult = function(res) {
            if(res) {
                setValue('consoleWeb' ,  res.value );
            }
        }
    </textarea>
    <br/>

    <div  cmptype="Edit" name="can_edit"   class='ctrl_edit editControl box-sizing-force' style = "width: 850;"   caption="Переменная"  height="40px"  disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"       onchange="D3Api.stopEvent(); "   /></div>
    <div  cmptype="Button" name="201181b43b8d11ec9f450242ac110002" onclick="Form.selectOkato()" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Модальное окно</div></div>
    
        <div  name="consoleWeb" cmptype="TextArea" title="" class="textArea box-sizing-force editControl" style="width:840px;height:320px"  left='10px' >
           <textarea cmpparse="TextArea"   >Результат</textarea>
        </div>

    <div name="can_edit"  class="ctrl_edit editControl box-sizing-force"  style=" width:60%; height:25px"  id="d3ctrl651601829680105">
        <div class="edit-input">
            <input text=""  value="Значение , которое парадается в модальное окно"  onchange="D3Api.stopEvent();"  style="width:200;height:75%;"/>
        </div>
    </div>



</div>
<div cmptype="sysinfo" style="display:none;"></div>