<div cmptype="Form" onshow="Form.onShowForm()" caption="Пример работает SQLite на Android устройстве">
    <cmpScript>
        <![CDATA[
            Form.onShowForm = function() {
            }
            Form.saveSqlite = function() {
                Android.insertJson("tab1",'{"pole1":123456}');
            }
            Form.readSqlite = function() {
                setValue('log',Android.getJsonArray("tab1",''));
            }
            Form.readSqliteOne = function() {
                setValue('log',Android.getJson("tab1",1));
            }
        ]]>
    </cmpScript>
    <cmpTextArea name="log" height="50%" />
    <cmpButton caption="записать" onclick="Form.saveSqlite()"/>
    <cmpButton caption="Читать" onclick="Form.readSqlite()"/>
    <cmpButton caption="Читать 1 запись" onclick="Form.readSqliteOne()"/>
</div>