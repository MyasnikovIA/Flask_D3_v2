<div cmptype="Form" class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" name="MAINFORM" title="Тестовое окно" >
    <cmpScript name="ffffff">
        <![CDATA[
            Form.onCreate = function() {
               setVar("form_params","dddddddd");
               refreshDataSet('DB_MyDataSet');
            }
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
            Form.MySendPHP = function() {
                openD3Form('Exsample/main',true)
            }
        ]]>
    </cmpScript>

    <cmpButton id='test' caption="запустить Action!!!!" btn="outline-primary" onclick="Form.MySendPHP()" ></cmpButton>

    <cmpDataSet name="DB_MyDataSet" query_type="server_python">
         aa=1111
         data = []
         data.append({"id":1,"FULLNAME":"text1"})
         data.append({"id":2,"FULLNAME":"text2"})
         data.append({"id":3,"FULLNAME":"text3"})
         data.append({"id":4,"FULLNAME":"text4"})
         data.append({"id":5,"FULLNAME":"text5"})
         data
        <cmpDataSetVar name="form_params"    src="form_params"   srctype="var"/>
    </cmpDataSet>
    <br/><br/><br/><br/>
<!-- ===============================            -->
     <cmpScript >
        <![CDATA[
            Form.onPopupHelpKinds = function(arg) {
               alert(arg)
            }
        ]]>
    </cmpScript>
    <component  cmptype="Edit" popupmenu="pHelpKinds" />
    <cmpPopupMenu name="pHelpKinds" onpopup="Form.onPopupHelpKinds(args[1]);">
        <cmpPopupItem caption="-"/>
    </cmpPopupMenu>
<!-- ===============================            -->

 <div cmptype="tmp" repeat="0" dataset="DB_MyDataSet" repeatername="rptDirLines">
         <cmpLabel data="caption:FULLNAME" name="PAT_AT"/>
 </div>

<!-- ===============================            -->
=================================================
    <br/>

         <cmpComboBox class="form-control" name="MySel" multiselect="true">
            <cmpComboItem caption="" value=""/>
            <cmpComboItem caption="2" value="2"/>
            <cmpComboItem caption="3" value="3"/>
            <cmpComboItem caption="4" value="4"/>
        </cmpComboBox>
=================================================

</div>

