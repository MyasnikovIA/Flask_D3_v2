<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="Тестовое окно" >
    <cmpScript name="MainScript">
       <![CDATA[
            Form.onCreate = function() {
                setVar("form_params22","12345");
                setVar("paramArrDS",{"testparam1":123,"testParam2":345});
                console.log("1111111111");
            }
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

            <!-- Правая панель -->
            <cmpLayoutContainer path="Tutorial/main"/>

        <!-- Разделительны элемент (горизонтальный) -->
        <cmpLayoutSplit orientation="horizon" direction="top"/>
        <cmpLayoutContainer  colspan="25" >
            Нижняя панель
        </cmpLayoutContainer>

    </cmpLayout>

</cmpForm>

