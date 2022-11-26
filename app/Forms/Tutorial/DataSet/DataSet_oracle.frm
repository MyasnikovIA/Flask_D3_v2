<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >

    <cmpScript name="main_script">
        <![CDATA[
            Form.onExecDS = function() {
               setVar("form_params","6808629");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data)
                   setCaption("JSONres", JSON.stringify(data));
               });
            }
        ]]>
    </cmpScript>
    <cmpDataSet name="DB_MyDataSet" activateoncreate="false">
        <![CDATA[
            select ID,FULLNAME
              from D_V_LPU
             where (id > :form_params)
        ]]>
        <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>
   <h1>Запрос в Oracle SQL</h1>
   <cmpButton caption="Запуск запроса D_V_LPU" onclick="Form.onExecDS()" />
   <br/>
   <cmpLabel name="JSONres" caption="----------------"/>
</div>
