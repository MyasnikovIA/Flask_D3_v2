<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="EventTest" >
    <cmpScript name="MainScript">
       <![CDATA[
            Form.onCreate = function() {
            }
             Form.myFunction = function(event) {
              var x = event.touches[0].clientX;
              var y = event.touches[0].clientY;
              setCaption('info',"---"+ x + ", " + y);
            }
            Form.onClick = function(event) {
                var ctrl = getControl('info');
                setCaption('info',"---"+ctrl.innerHTML+"=="+event+"-----");
                /*
                var txt = "";
                var touch = event.targetTouches[0];
                // Place element where the finger is
                // obj.style.left = touch.pageX + 'px';
                // obj.style.top = touch.pageY + 'px';
                txt += "<br/>"+event;
                setCaption('info',"---"+txt+"-----");
                */
            }
       ]]>
    </cmpScript>
<div cmptype="tmp" ontouchmove="myFunction(event)"  style="background-color: #74992e;">
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa dasdfasdfasdfasdfasdfasdfsa
    <br/> <cmpLabel name="info" caption="fffffffffffffffffff"/>
</div>
</cmpForm>

