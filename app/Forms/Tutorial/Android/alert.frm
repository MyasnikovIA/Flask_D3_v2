<div cmptype="Form" onshow="Form.onShowForm()" caption="Пример работает только на клиенте D3extClient (Android)">
    <cmpScript>
        <![CDATA[
            Form.onShowForm = function() {
               if (typeof Android === 'undefined') {
                   getControl("alert_message").style.display='block';
               }else{
                   getControl("alert_message").style.display='none';
               }
            }
        ]]>
    </cmpScript>
     <div cmptype="tmp" name="alert_message">
          <h1>Функционал работать не будет , так как вы запустили форму не из  D3extClient (Android) </h1>
     </div>
     <cmpButton caption="Alert"  onclick=" Android.alert('Tutorial/Android/alert')" />
     <cmpButton caption="Console.log"  onclick=" log('Tutorial/Android/alert',{'sdfsafsadf':'222222222'})" />
     <cmpButton caption="Console.log 2"  onclick=" console_log('Tutorial/Android/alert',{'sdfsafsadf':'32423423'})" />
</div>