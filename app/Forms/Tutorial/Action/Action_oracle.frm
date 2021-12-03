<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

   <cmpScript name="main_script">
       <![CDATA[
            Form.onExecAction = function() {
               executeAction('getMyDataSet');
            }
            Form.onExecActionV2 = function() {
               setVar("form_params","6808629");
               setVar("DIR_NUMB","test var 2");
               executeAction('getMyActionV2', function(){
                  console.log("DIR_NUMB", DIR_NUMB);
               });
            }

       ]]>
   </cmpScript>
    <cmpAction name="getMyAction" activateoncreate="true">
        <![CDATA[
          begin
            :CTRL_NUMB := 'Запрос из getMyDataSet: 123456 ';
          end;
        ]]>
        <cmpActionVar name="CTRL_NUMB"   src="CTRL_NUMB:caption"   srctype="ctrl" put="" />
   </cmpAction>

   <cmpButton caption="Запуск запроса getMyAction" onclick="Form.onExecAction()" />
   <cmpLabel name="CTRL_NUMB" caption="-----" />
   <br/>
   <br/>
   <br/>

   <cmpAction name="getMyActionV2" activateoncreate="true">
        <![CDATA[
          begin
            :DIR_NUMB     := '111111111111--'||:form_params;
            :RESULT_LABEL := 'cmpEdit=' || :CTRL_INP ;
          end;
        ]]>
        <cmpActionVar name="form_params"   src="form_params" srctype="var" />
        <cmpActionVar name="DIR_NUMB"      src="DIR_NUMB:caption"      put="" srctype="ctrl"/>
        <cmpActionVar name="RESULT_LABEL"  src="RESULT_LABEL:caption"  put="" srctype="ctrl"/>
        <cmpActionVar name="CTRL_INP"      src="CTRL_INP"    srctype="ctrl" />
   </cmpAction>
   <br/>
   <cmpButton caption="Запуск запроса getMyActionV2" onclick="Form.onExecActionV2()" />
   <cmpEdit name="CTRL_INP"  />
   <br/>
    <cmpLabel name="RESULT_LABEL" caption="-----" />
   <br/>
    <cmpLabel name="DIR_NUMB" caption="-----" />

</div>
