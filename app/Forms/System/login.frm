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

                //executeAction('Authorization', function() {
                //  console.log("Result",getVar("Result"));
                //})
            };
            Form.Submit2 = function() {
                var login = getValue('DBLogin').split(/\[(.*?)\]/, 2);
                setValue('DBLogin', (login[0] || "").toUpperCase());
                setVar('DBLoginProxy', login[1]);
                executeModule('Authorization2', function() {

                })
            };
       ]]>
    </cmpScript>
    <cmpModule  name="Authorization" mode="post" module="System/Authorization">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
    <cmpModule  name="Authorization2" mode="post" module="System/AuthorizationV2:ExecModuleEny.test">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
      <cmpAction name="Authorization" activateoncreate="true" query_type="server_python">
            <![CDATA[
                print("DBLogin",DBLogin)
                print("DBPassword",DBPassword)
                SQL = psycopg2.connect(database='flask_db', user=DBLogin, password=DBPassword, host='127.0.0.1', port=5432)


                DB = psycopg2.connect(database='flask_db', user='postgres', password='postgres', host='127.0.0.1', port=5432)

                print("psycopg2",psycopg2)
                print(SQL)
                """
                # 'DatabaseName': 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask_db',
                ip = '127.0.0.1'
                port = 5432
                SID = 'flask_db'
                import psycopg2
                DB["DB"] = psycopg2.connect(database='flask_db', user=DBLogin, password=DBPassword, host='127.0.0.1', port=5432)
                #session["DB"].autocommit = True
                print(session)
                """
            ]]>
            <cmpActionVar name="DBLogin"    src="DBLogin"     srctype="ctrl" get="" />
            <cmpActionVar name="DBPassword" src="DBPassword"  srctype="ctrl" get="" />
            <cmpActionVar name="result"     src="Result"      srctype="var" put="" />
       </cmpAction>

    <center>
        <table>
            <tr>
                <td>
                    <cmpLabel caption="Имя пользователя"/>
                </td>
                <td>
                    <cmpEdit name="DBLogin"/>
                </td>
            </tr>
            <tr>
                <td>
                    <cmpLabel caption="Пароль пользователя"/>
                </td>
                <td>
                    <cmpEdit name="DBPassword"/>
                </td>
            </tr>
            <tr>
                <td  colspan="2" >
					<cmpButton onclick="Form.Submit();" caption="Войти" name="btnLogin"/>
                </td>
            </tr>
            <tr>
                <td  colspan="2" >
					<cmpButton onclick="Form.Submit2();" caption="Войти2" name="btnLogin"/>
                </td>
            </tr>

        </table>
    </center>
</div>
