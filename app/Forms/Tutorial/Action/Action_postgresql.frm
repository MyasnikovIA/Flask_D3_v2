<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

   <cmpScript name="main_script">
       <![CDATA[
            Form.onExecAction = function() {
               executeAction('getMyAction');
            }
            Form.onExecActionV2 = function() {
               setVar("form_params","6808629");
               setVar("DIR_NUMB","test var входящее");
               executeAction('getMyActionV2', function(){
                  console.log("DIR_NUMB", getVar("DIR_NUMB"));
               });
            }
            Form.onExecActionV3 = function() {
               executeAction('getMyActionV3', function(){
                  console.log("DIR_NUMB2", getValue("DIR_NUMB2"));
               });
            }
       ]]>
   </cmpScript>
   <cmpAction name="getMyAction" activateoncreate="true">
       <![CDATA[
          select 'Запрос из getMyDataSet: 123456 ' as CTRL_NUMB
       ]]>
       <cmpActionVar name="ctrl_numb"   src="CTRL_NUMB:caption"   srctype="ctrl" put="" />
   </cmpAction>
   <cmpButton caption="Запуск запроса getMyAction" onclick="Form.onExecAction()" />
   <cmpLabel name="CTRL_NUMB" caption="-----" />
   <br/>
   <br/>=============================================================================
   <cmpAction name="getMyActionV2" activateoncreate="true">
        <![CDATA[
          select
             'Переменная измененая в Actio = '||%(form_params)s as DIR_NUMB
            ,'cmpEdit=' || %(CTRL_INP)s as RESULT_LABEL
        ]]>
        <cmpActionVar name="form_params"   src="form_params" srctype="var" />
        <cmpActionVar name="DIR_NUMB"      src="DIR_NUMB:caption"      put="" srctype="ctrl"/>
        <cmpActionVar name="DIR_NUMB"      src="DIR_NUMB"              put="" srctype="var" />
        <cmpActionVar name="result_label"  src="RESULT_LABEL:caption"  put="" srctype="ctrl"/>
        <cmpActionVar name="CTRL_INP"      src="CTRL_INP"    srctype="ctrl" />
   </cmpAction>

   <br/>
    <cmpButton caption="Запуск запроса getMyActionV2" onclick="Form.onExecActionV2()" />
    <cmpEdit name="CTRL_INP"  />
   <br/>
    <cmpLabel name="RESULT_LABEL" caption="-----" />
   <br/>
    <cmpLabel name="DIR_NUMB" caption="-----" />
   <br/>=============================================================================
      <cmpAction name="getMyActionV3" activateoncreate="true" query_type="server_python">
            <![CDATA[
                DIR_NUMB2 = "dddddddddddddddddddddddd"
            ]]>
            <cmpActionVar name="DIR_NUMB2"      src="DIR_NUMB2"   put="" srctype="var" />
      </cmpAction>
      <cmpButton caption="Запуск запроса getMyActionV3" onclick="Form.onExecActionV3()" />
      <cmpLabel name="DIR_NUMB2" caption="-----" />

</div>
