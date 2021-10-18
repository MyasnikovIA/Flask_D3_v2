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

    <cmpButton caption="Form.openD3Form" onclick="Form.openD3Form();"/>

    <cmpLayout name="test" >
        <cmpLayoutContainer  colspan="22"  style="height:25px">
            верх444
              <cmpLabel caption="Лево"/>
            555
        </cmpLayoutContainer>
        <cmpLayoutSplit orientation="horizon"/>
            <cmpLayoutContainer>
                1111
                <cmpLabel caption="Лево"/>
                4444
            </cmpLayoutContainer>
            <cmpLayoutSplit orientation="vertical"/>
            <cmpLayoutContainer>
                2222
                <cmpLabel caption="Центр"/>
                4444
                <cmpEdit name="test3"/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <cmpEdit name="test3"/>
            </cmpLayoutContainer>
            <cmpLayoutSplit orientation="vertical"/>
            <cmpLayoutContainer>
                3333
                <cmpLabel caption="право"/>
                4444
            </cmpLayoutContainer>
        <cmpLayoutSplit orientation="horizon"/>
        <cmpLayoutContainer  colspan="25">
            Низ
        </cmpLayoutContainer>
    </cmpLayout>

</cmpForm>

