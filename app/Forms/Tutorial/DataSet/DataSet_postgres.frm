<div cmptype="Form"  caption="Выполнение SQL запросов" width="60%" height="60%" >
    <cmpScript name="main_script">
        <![CDATA[
            Form.onExecDS = function() {
               setVar("form_params","schemaname");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data);
                   setCaption("JSONres", JSON.stringify(data));
               });
            }
        ]]>
    </cmpScript>
    <cmpDataSet name="DB_MyDataSet" activateoncreate="false">
        <![CDATA[
            SELECT table_name,
                   column_name,
                   data_type
              FROM information_schema.columns
             WHERE column_name = %(form_params)s
        ]]>
       <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>
    <h1>Запрос в PostgressSQL</h1>
    <cmpButton caption="Запуск запроса (information_schema.columns)" onclick="Form.onExecDS()" />
    <br/>
    <cmpLabel name="JSONres" caption="----------------"/>
</div>


