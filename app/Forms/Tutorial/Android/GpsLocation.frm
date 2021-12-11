<div cmptype="Form" onshow="Form.onShowForm()" caption="Пример работает GPS">
    <cmpScript>
        <![CDATA[
            Form.onShowForm = function() {
            }
            Form.getLocation = function() {
                setValue('log',Android.getLocation());
            }

            Form.startGPS = function() {
               Android.startGPS();
            }
            Form.stopGPS = function() {
                Android.stopGPS();
            }

        ]]>
    </cmpScript>
    <cmpTextArea name="log" height="50%" />
         <cmpButton caption="Включить GPS" onclick="Form.onGPS()"/>
    <br/><cmpButton caption="Получить координаты getLocation" onclick="Form.getLocation()"/>
    <br/><cmpButton caption="Выключить GPS" onclick="Form.offGPS()"/>

</div>

