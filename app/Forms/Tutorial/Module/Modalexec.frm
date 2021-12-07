<div cmptype="Form" caption="Выполнение SQL запросов" width="60%" height="60%" >
    <cmpScript name="main_script">
        <![CDATA[
            Form.Submit = function() {
                executeModule('Authorization');
            };
            Form.Submit2 = function() {
                executeModule('Authorization2');
            };
       ]]>
    </cmpScript>
    <cmpModule  name="Authorization" mode="post" module="Tutorial/Module/ModulExecTextV1">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
    <cmpModule  name="Authorization2" mode="post" module="Tutorial/Module/ModulExecTextV2:ExecModuleEny.test">
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
