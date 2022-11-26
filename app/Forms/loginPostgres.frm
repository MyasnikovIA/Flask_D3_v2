<div cmptype="Form"  name="MAINFORM" width="60%" height="60%"  caption="Авторизоваться в системе" >
    <cmpScript>
        <![CDATA[
           Form.login = function() {
               executeAction('loginDB', function() {
                   if (getVar("resText").length === 0){
                       close({connect: true});
                   } else {
                       alert("resText: "+getVar("resText"));
                   }
               });
            };
        ]]>
    </cmpScript>
    <cmpAction name="loginDB" activateoncreate="true" query_type="server_python">
         <![CDATA[
             resText = ""
             resConnect = connectPostgres(session,SrvName, int(PortName),DataBaseName, LogName, LogPass)
             if resConnect[0] == False:
                resText = f"Ошибка подключения к БД:{resConnect[1]}"
             else:
                resText = ""
         ]]>
         <cmpActionVar name="SrvName" src="SrvName" srctype="ctrl" />
         <cmpActionVar name="PortName" src="PortName" srctype="ctrl" />
         <cmpActionVar name="DataBaseName" src="DataBaseName" srctype="ctrl" />
         <cmpActionVar name="LogPass" src="LogPass" srctype="ctrl" />
         <cmpActionVar name="LogName" src="LogName" srctype="ctrl" />
         <cmpActionVar name="resText" src="resText" srctype="var" put=""/>
    </cmpAction>
    <table style="text-align: center">
        <tr>
            <td>
                <cmpLabel caption="Адрес сервера "/>
            </td>
            <td>
                <cmpEdit name="SrvName" value="192.168.0.224"/>
            </td>
        </tr>
        <tr>
            <td>
                <cmpLabel caption="Порт сервера "/>
            </td>
            <td>
                <cmpEdit name="PortName" value="5432"/>
            </td>
        </tr>
        <tr>
            <td>
                <cmpLabel caption="Имя базы даных"/>
            </td>
            <td>
                <cmpEdit name="DataBaseName" value="postgres" type="text"/>
            </td>
        </tr>
        <tr>
            <td>
                <cmpLabel caption="Имя пользователя "/>
            </td>
            <td>
                <cmpEdit name="LogName" value="d3user"/>
            </td>
        </tr>
        <tr>
            <td>
                <cmpLabel caption="Пароль пользователя "/>
            </td>
            <td>
                <cmpEdit name="LogPass"  value="" type="password"/>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <cmpButton caption="Зарегистрироваться в системе"  onclick="Form.login();" />
            </td>
        </tr>
    </table>
</div>
