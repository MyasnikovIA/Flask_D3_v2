<div cmptype="Form" caption="Выполнение SQL запросов" width="60%" height="60%" oncreate = "Form.create();" >
    <cmpScript name="main_script">
        <![CDATA[
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
       ]]>
    </cmpScript>
    <cmpModule  name="Authorization" mode="post" module="System/AuthorizationPostrges">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
    <center>
        <table>
            <tr>
                <td>
                    <cmpLabel caption="Имя пользователя"/>
                </td>
                <td>
                    <cmpEdit name="DBLogin" value="postgres"/>
                </td>
            </tr>
            <tr>
                <td>
                    <cmpLabel caption="Пароль пользователя"/>
                </td>
                <td>
                    <cmpEdit name="DBPassword" value="postgres"/>
                </td>
            </tr>
            <tr>
                <td  colspan="2" >
					<cmpButton onclick="Form.Submit();" caption="Войти" name="btnLogin"/>
                </td>
            </tr>
        </table>
    </center>

    <cmpScript name="main_script_test" >
        <![CDATA[
            Form.onExecDS = function() {
               setVar("form_params","schemaname");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data);
                   setCaption("JSONres", JSON.stringify(data));
               });
            }
        ]]>
    </cmpScript>
    <!--
        database="oracle" - имя конфигурации которая будет использоватся при запуске запроса
        Если этот параметр не будет указан, тогда  запрос будет выполнен в первом попавшемся подключении
    -->
    <cmpDataSet name="DB_MyDataSet" activateoncreate="false" database="postgre">
        <![CDATA[
            SELECT table_name,
                   column_name,
                   data_type
              FROM information_schema.columns
             WHERE column_name = %(form_params)s
        ]]>
       <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>
    <h1>Запрос в PostgressSQL</h1>
    <cmpButton caption="Запуск запроса (information_schema.columns)" onclick="Form.onExecDS()" />
    <br/>
    <cmpLabel name="JSONres" caption="----------------"/>

</div>
