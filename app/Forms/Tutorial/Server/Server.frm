<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="Пример компонента Tabs (необходимо дописать)" >
    <cmpScript name="MainScript">
       <![CDATA[
          Form.onCreate = function() {
              console.log( #server(..testscript,111,2222,"sssssssss",'wqerwrw')# );
          }
          Form.MyColl = function(arg) {
              console.log("MyColl", arg );
              console.log("getVar('test')", getVar('test') );
          }
       ]]>
    </cmpScript>
    <cmpServer name="testscript" args="testVar1;testvar2">
        test = testVar1 + testvar2
    </cmpServer>


    <cmpButton  caption="выполнить" onclick="#server(..scriptColl,Form.MyColl,'Arg1','Arg2','Arg3')# "/>
    <cmpServer name="scriptColl" args="testVar1;testvar2;testvar3">
       <![CDATA[
            test = {'test':1111, 'test2':3333, 'arg3':testVar1, 'arg4':testvar2, 'arg4':testvar3}
       ]]>
    </cmpServer>

</cmpForm>

