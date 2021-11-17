<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

    <cmpScript name="main_script">
        <![CDATA[
            Form.onExecDS = function() {
               setVar("form_params","6808629");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data)
               });
            }
        ]]>
    </cmpScript>
    <cmpDataSet name="DB_MyDataSet" activateoncreate="false">
        <![CDATA[
            select ID,FULLNAME
              from D_V_LPU
             where  (id > :form_params)
        ]]>
        <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>
   <cmpButton caption="Запуск запроса" onclick="Form.onExecDS()" />

</div>
