<div cmptype="Form" width="60%" height="60%" caption="Компонент cmpOpenStreetMap в разработке">
   <cmpScript>
        <![CDATA[
           Form.setInfo = function(data){
                console.log(data);
           }
           Form.foundGeoObject = function() {
                D3Api.OpenStreetMapCtrl.getGisObjest(getValue("find"));
           };
        ]]>
   </cmpScript>
   <cmpLabel name="info" caption="sfsfsadf"/>
   <cmpEdit name="find"  value="Барнаул" /> <cmpButton caption="Установить метку на геоточку" onclick="Form.foundGeoObject();"/>
   <cmpOpenStreetMap  onclickmap="Form.setInfo(data)"  height="640px">
   <!--width="800px" height="640px"-->
   </cmpOpenStreetMap>
</div>
