
        <html  lang="en"  ><head>
            <meta charset="UTF-8"/>
            <title>Title</title>
            <link rel="stylesheet"  type="text/css"  href="./~d3theme"/>
            <script src="./~d3main"></script></head>
            <body>
        <div  cmptype="Base" name="aa593836576b11ecabc3001a7dda7108" caption="Выполнение SQL запросов"  width="60%"  height="60%"  oncreate="Form.create();"  formName="System/loginPostgres.frm" >

    <textarea cmptype="Script" name="main_script" style="display:none;">
        
            Form.create = function(){
                ['DBLogin', 'DBPassword'].forEach((ctrl) => setControlProperty(ctrl, 'enabled', true));
                setAttribute(getDomBy(getControl('DBPassword'), 'input'), 'type', 'password');
                var loginCtrl = getControl('DBLogin');
                addEvent(loginCtrl, 'paste', function() {
                    setTimeout(function() {
                        var login = getValue('DBLogin');
                        var arr = login.match(/(^[^/]+)\/(.*)/);
                        if (arr && arr[1]) {
                            setValue('DBLogin', arr[1].trim());
                        }
                        if (arr && arr[2]) {
                            setValue('DBPassword', arr[2].trim());
                        }
                    });
                });
            }
            Form.Submit = function() {
                var login = getValue('DBLogin').split(/\[(.*?)\]/, 2);
                setValue('DBLogin', (login[0] || "").toUpperCase());
                setVar('DBLoginProxy', login[1]);
                executeModule('Authorization', function() {

                })
            };
       
    </textarea>
    
        
    
    <center>
        <table>
            <tr>
                <td>
                    
                <span  cmptype="Label" name="aa5a70b5576b11eca0ae001a7dda7108"  class='label'    > Имя пользователя </span>
                </td>
                <td>
                    <div  cmptype="Edit" name="DBLogin"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"     disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"   value="postgres"      onchange="D3Api.stopEvent(); "   /></div>
                </td>
            </tr>
            <tr>
                <td>
                    
                <span  cmptype="Label" name="aa5ae645576b11ec91d1001a7dda7108"  class='label'    > Пароль пользователя </span>
                </td>
                <td>
                    <div  cmptype="Edit" name="DBPassword"   class='ctrl_edit editControl box-sizing-force' style = "width: 100%;"     disabled onchange="D3Api.stopEvent();">
                        <input cmpparse="Edit"   type = "text"   value="postgres"      onchange="D3Api.stopEvent(); "   /></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
					<div  cmptype="Button" name="btnLogin" onclick="Form.Submit();" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Войти</div></div>
                </td>
            </tr>
        </table>
    </center>

    <textarea cmptype="Script" name="main_script_test" style="display:none;">
        
            Form.onExecDS = function() {
               setVar("form_params","schemaname");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data);
                   setCaption("JSONres", JSON.stringify(data));
               });
            }
        
    </textarea>
    
    
    
    <h1>Запрос в PostgressSQL</h1>
    <div  cmptype="Button" name="aa5ba97b576b11ec93fa001a7dda7108" onclick="Form.onExecDS()" tabindex="0"  class='ctrl_button box-sizing-force' style="width: 255px"  ><div class="btn_caption btn_center " >Запуск запроса (information_schema.columns)</div></div>
    <br/>
    
                <span  cmptype="Label" name="JSONres"  class='label'    > ---------------- </span>

</div></body></html>
<div cmptype="sysinfo" style="display:none;"><Module name="Authorization"  activateoncreate="true">
<var get='DBPassword' src="DBPassword" srctype="ctrl"></var>
<var get='DBLogin' src="DBLogin" srctype="ctrl"></var></Module><DataSet name="DB_MyDataSet" mode="Range" activateoncreate="false"><Var get='form_params'  src="form_params" srctype="var"></Var></DataSet></div>