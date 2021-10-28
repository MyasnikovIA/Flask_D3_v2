<div cmptype="Form" caption="" width="60%" height="60%">
    <cmpScript>
        <![CDATA[
            Form.onBtnTest2 = function() {
              setVisible('d_wg_delete_Ctrl', true);
            }
            Form.onBtnTest3 = function() {
              var win3 = new DConfirmWindow("Вы уверены...?", function(){ console.log('вы нажали OK');}, function(){ console.log('вы нажали отмена');} );
              win3.show();
            }
        ]]>
    </cmpScript>
   <cmpButton onclick="Form.onBtnTest3();" caption="Error"/>
   <cmpButton onclick="Form.onBtnTest2();" caption="ffasdfgsd"/>
<!--
    http://192.168.15.200:9091/getform.php?cache_enabled=0&modal=1&Form=Tutorial%2FDialog%2FDialog&cache=c865f9af408fb94ce38db76e0b211b032&blockName=d_wg_delete_Ctrl
-->
    <h1>Дописать пример!!!</h1>
    <cmpDialog name="d_wg_delete_Ctrl" show_buttons="false">
        <div style="text-align: center;">
            <cmpLabel caption="Какой то текст1"/>
        </div>
        <div style="text-align: center;">
         <cmpButton caption="Какая то кнопка2"/>
        </div>
    </cmpDialog>
    <h1>Дописать пример!!!</h1>
</div>
