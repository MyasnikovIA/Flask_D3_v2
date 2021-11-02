<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" name="MAINFORM" title="Тестовое окно" >
    <cmpScript name="MainScript">
       <![CDATA[
            Form.onCreate = function() {
                setVar("form_params22","12345");
                setVar("paramArrDS",{"testparam1":123,"testParam2":345});
                console.log("1111111111");
            }
            Form.testClick = function() {
               console.log("4444444444");
               setValue('myedit','sssss');
            }

            Form.testClick2 = function() {
               setVar("myedit2",11);
               executeAction("MyAction",function(){
                  console.log("0980989098");
                  console.log(getVar("myedit2"));
               })
            }
            Form.refrashDS = function() {
               setVar("myedit2",11);
               refreshDataSet('DB_MyDataSet', function() {
                 var data = getDataSet('DB_MyDataSet').data;
                   // if (!empty(data)) {}
                   console.log("data",data)
                   getDataSet('DB_MyDataSet').setData([{"id":1,"FULLNAME":"text1"},{"id":2,"FULLNAME":"text2"},{"id":3,"FULLNAME":"text3"}]);

                     DErrorWindow(getDataSet('DB_MyDataSet').data)
               });
            }



            Form.openD3Form = function() {
                openD3Form('main',true,{width: '100%', height: "100%", vars: { AGENT_ID: 123 }, onclose: function(mod) { console.log('mod',mod); }} );
            }

       ]]>
    </cmpScript>

    <cmpButton name ="Button1" caption="test" onclick="Form.testClick();"/>
    <cmpButton caption="testClick2" onclick="Form.testClick2();"/>
    <cmpButton caption="Form.refrashDS" onclick="Form.refrashDS();"/>
    <cmpButton caption="Form.openD3Form" onclick="Form.openD3Form();"/>
    <cmpEdit name="myedit"/>
      <cmpDataSet name="DB_MyDataSet" query_type="server_python"  activateoncreate="true">
         <![CDATA[
             aa=form_params
             # bb=paramArrDS
             # myedit = form_params
             data = []
             data.append({"id":1,"FULLNAME":"text1"})
             data.append({"id":2,"FULLNAME":"text2"})
             data.append({"id":3,"FULLNAME":"text3"})
             data.append({"id":4,"FULLNAME":"text4"})
             data.append({"id":5,"FULLNAME":defVAR})
             data
         ]]>
         <cmpDataSetVar name="LPU" src="LPU" srctype="session"/>
         <cmpDataSetVar name="form_params"   src="form_params22"    srctype="var"/>
         <cmpDataSetVar name="paramArrDS"    src="paramArr"       srctype="var"/>
         <cmpDataSetVar name="defVAR"        src="defVAR"         srctype="var"   default="11111"/>
         <cmpDataSetVar name="myedit"        src="myedit"         srctype="ctrl" />
      </cmpDataSet>
      <cmpAction name="MyAction" query_type="server_python">
         <![CDATA[
           myedit = form_params
         ]]>
         <cmpActionVar name="LPU"                                         srctype="session"/>
         <cmpActionVar name="form_params"   src="form_params22"   get=""  srctype="var"/>
         <cmpActionVar name="paramArrDS"    src="paramArr"       get=""  srctype="var"/>
         <cmpActionVar name="myedit"        src="myedit"         put=""  srctype="ctrl"/>
         <cmpActionVar name="myedit2"       src="myedit2"        put=""  srctype="var"/>
      </cmpAction>

     <div cmptype="tmp" name="lpuNameData" dataset="DB_MyDataSet" repeat="0" >
            <cmpLabel data="caption:id"/>
            <cmpLabel data="caption:FULLNAME"/>
    </div>
    <cmpButton onclick="close({'test':111 })" caption="закрыть"/>

</cmpForm>

