<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" name="MAINFORM" caption="Тестовое окно" >
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

            Form.getLay = function(){
               console.log( getControl("MyLayout"));
            };



       ]]>
    </cmpScript>

    <cmpButton caption="Form.openD3Form" onclick="Form.openD3Form();"/>
    <cmpButton caption="Form.MyLayout" onclick="Form.getLay();"/>

    <cmpLayout name="MyLayout"  style="height:90%">

        <cmpLayoutContainer  colspan="22"  style="height:125px">
              <cmpLabel caption="Верхняя панель"/>
        </cmpLayoutContainer>

        <!-- Разделительны элемент (горизонтальный) -->
        <cmpLayoutSplit orientation="horizon" direction="top" />

             <!-- контейнер -->
             <cmpLayoutContainer>
                <cmpLabel caption="Левая панель "/>
            </cmpLayoutContainer>

            <!-- Разделительны элемент (вертикальный) -->
            <cmpLayoutSplit orientation="vertical"/>


            <cmpLayoutContainer>
                <cmpLabel caption="Центральная панель"/>
                <cmpEdit name="test3"/>
                <cmpEdit name="test3"/>
            </cmpLayoutContainer>

            <!-- Разделительны элемент (вертикальный) -->
            <cmpLayoutSplit orientation="vertical"/>

            <cmpLayoutContainer>
                <cmpLabel caption="Правая панель"/>
            </cmpLayoutContainer>

        <!-- Разделительны элемент (горизонтальный) -->
        <cmpLayoutSplit orientation="horizon" direction="top"/>
        <cmpLayoutContainer  colspan="25" >
            Нижняя панель
        </cmpLayoutContainer>

    </cmpLayout>

</cmpForm>

