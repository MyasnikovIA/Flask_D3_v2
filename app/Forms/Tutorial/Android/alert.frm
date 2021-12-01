<div cmptype="Form" onshow="Form.onShowForm()" caption="Пример работает только на клиенте D3extClient (Android)">
    <cmpScript>
        <![CDATA[
            Form.onShowForm = function() {
               if (typeof Android === 'undefined') {
                   getControl("alert_message").style.display='block';
               } else {
                   getControl("alert_message").style.display='none';
               }
                var canvas = getControl("canvas");
                canvas.addEventListener('touchstart', Form.touchstartListener, false);
                canvas.addEventListener('touchmove', Form.touchmoveListener, false);
                canvas.addEventListener('touchend', Form.touchendListener, false);
                canvas.addEventListener('touchenter', Form.touchenterListener, false);
                canvas.addEventListener('touchleave', Form.touchleaveListener, false);
                canvas.addEventListener('touchcancel', Form.touchcancelListener, false);
            }

            window.RecognizerText = function(text) {
               setValue('sendText',text);
            }

            // обработка тачпада
            Form.touchstartListener = function(event){
                var msg="touchstart - >";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchstart - >"+ event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }
            Form.touchmoveListener = function(event){
                var msg="touchmove - ";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchmove - "+ event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }
            Form.touchendListener = function(event){
                var msg="touchend - ";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchend - "+ event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }
            Form.touchenterListener = function(event){
                var msg="touchenter - ";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchenter - " + event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }
            Form.touchleaveListener = function(event){
                var msg="touchleave - ";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchleave - " + event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }
            Form.touchcancelListener = function(event){
                var msg="touchcancel - ";
                for (let touch of event.changedTouches) {
                   msg += "("+touch.pageX + ":" + touch.pageY+")";
                }
                setCaption("info",msg);
                // setCaption("info","touchcancel - " + event.changedTouches[0].pageX + ":" + event.changedTouches[0].pageY);
                event.preventDefault();
            }

        ]]>
    </cmpScript>
     <div cmptype="tmp" name="alert_message">
          <h1>Функционал работать не будет , так как вы запустили форму не из  D3extClient (Android) </h1>
     </div>
     <cmpEdit name="sendText" /> <cmpButton onclick=" Android.speech( getValue('sendText') ); " caption="проговорить текст" />

     <cmpButton caption="Alert"  onclick=" Android.alert('Tutorial/Android/alert')" />
     <cmpButton caption="Console.log"  onclick=" log('Tutorial/Android/alert',{'sdfsafsadf':'222222222'})" />
     <cmpButton caption="Console.log 2"  onclick=" console_log('Tutorial/Android/alert',{'sdfsafsadf':'32423423'})" />
     <div cmptype="tmp"  style="background-color: #74992e;" name="canvas" >
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
     </div>
     <h1>
          <cmpLabel name="info" caption="События тачпада"/>
     </h1>
</div>