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

    <cmpModule  name="Authorization" mode="post" module="System/AuthorizationOracle">
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
                    <cmpEdit name="DBLogin" value="dev"/>
                </td>
            </tr>
            <tr>
                <td>
                    <cmpLabel caption="Пароль пользователя"/>
                </td>
                <td>
                    <cmpEdit name="DBPassword" value="def"/>
                </td>
            </tr>
            <tr>
                <td  colspan="2" >
					<cmpButton onclick="Form.Submit();" caption="Войти" name="btnLogin"/>
                </td>
            </tr>
        </table>
    </center>
</div>
