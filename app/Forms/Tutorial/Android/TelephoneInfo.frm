<div cmptype="Form" caption="Пример работает SQLite на Android устройстве" onshow="Form.onShow()">
<cmpScript>
  <![CDATA[
      Form.onShow = function(){
          if (typeof(Android) !== 'undefined') {
             setValue('log','--------');
          }
      }
      Form.setTelephoneSetings = function() {
          if (typeof(Android) !== 'undefined') {
             Android.setTelephoneSetings();
          }
      }
      Form.getDeviceInfo = function() {
          if (typeof(Android) !== 'undefined') {
              setValue('log',Android.getDeviceInfo());
          }
      }

  ]]>
</cmpScript>
<cmpTextArea name="log" height="50%"/>
<cmpButton caption="setTelephoneSetings Получить разрешение на получение данных телефона" onclick="Form.setTelephoneSetings()"/>
<cmpButton caption="getDeviceInfo получить JSON объект " onclick="Form.getDeviceInfo()"/>
</div>