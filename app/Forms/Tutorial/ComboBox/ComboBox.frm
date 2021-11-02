<div cmptype="Form"  caption="" width="60%" height="60%"  oncreate="Form.onCreate()" >

    <cmpScript name="main_script">
        <![CDATA[
            Form.onCreate = function() {
               setVar("form_params","dddddddd");
               refreshDataSet('DB_MyDataSet', function(){
                   var data = getDataSet('DB_MyDataSet').data;
                   console.log("data",data)
               });
            }
        ]]>
    </cmpScript>

    <cmpDataSet name="DB_MyDataSet" query_type="server_python"  activateoncreate="false">
        aa=1111
        data = []
        data.append({"ID":5,"FULLNAME":"text1"})
        data.append({"ID":6,"FULLNAME":"text2"})
        data.append({"ID":7,"FULLNAME":"text3"})
        data.append({"ID":8,"FULLNAME":"text4"})
        data.append({"ID":9,"FULLNAME":"text5"})
        data
        <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>

    <cmpComboBox class="form-control" name="MySel" multiselect="true">
        <cmpComboItem caption="" value=""/>
        <cmpComboItem caption="2" value="2"/>
        <cmpComboItem caption="3" value="3"/>
        <cmpComboItem caption="4" value="4"/>
        <cmpComboItem dataset="DB_MyDataSet" repeat="0" data="value:ID;caption:FULLNAME;"  repeatername="rptDirLines"/>
    </cmpComboBox>

    <cmpComboBox class="form-control" name="MySel2" >
        <cmpComboItem caption="4" value="4"/>
        <cmpComboItem caption="2" value="2"/>
        <cmpComboItem caption="3" value="3"/>
        <cmpComboItem dataset="DB_MyDataSet" repeat="0" data="value:ID;caption:FULLNAME;"  repeatername="rptDirLines"/>
    </cmpComboBox>

</div>
