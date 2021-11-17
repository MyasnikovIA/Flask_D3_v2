<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

   <cmpScript name="main_script">
       <![CDATA[
            Form.onExecDS = function() {
               setVar("form_params","6808629");
               executeAction('getMyDataSet', function(){

               });
            }
       ]]>
   </cmpScript>
   <cmpAction name="getMyDataSet" activateoncreate="true">
        <![CDATA[
          begin
            :DIR_NUMB := '111111111111'||:form_params;
            :CTRL_NUMB := 'cmpEdit=' || :CTRL_INP ;
          end;
        ]]>
        <cmpActionVar name="form_params" src="form_params" srctype="var" />
        <cmpActionVar name="DIR_NUMB"    src="DIR_NUMB"    srctype="var"  put="" />
        <cmpActionVar name="CTRL_NUMB"   src="CTRL_NUMB:caption"   srctype="ctrl" put="" />
        <cmpActionVar name="CTRL_INP"    src="CTRL_INP"    srctype="ctrl" />
   </cmpAction>
   <cmpButton caption="Запуск запроса" onclick="Form.onExecDS()" />
   <cmpLabel name="CTRL_NUMB" caption="-----" />
   <cmpEdit name="CTRL_INP"  />

</div>
