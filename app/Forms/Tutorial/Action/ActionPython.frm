

<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

   <cmpScript name="main_script">
       <![CDATA[
            Form.onExecDS = function() {
               executeAction('getMyActionV3', function(){
                   alert("DIR_NUMB2: "+getVar("DIR_NUMB2"));
               });
            }
       ]]>
   </cmpScript>
      <cmpAction name="getMyActionV3" activateoncreate="true" query_type="server_python">
            <![CDATA[
                DIR_NUMB2 = "locals()"
            ]]>
            <cmpActionVar name="DIR_NUMB2"      src="DIR_NUMB2"   put="" srctype="var" />
      </cmpAction>
   <cmpButton caption="Запуск запроса" onclick="Form.onExecDS()" />
</div>




