<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="Пример компонента Tabs (необходимо дописать)" >
    <cmpScript name="MainScript">
       <![CDATA[
            Form.onCreate = function() {
            }
       ]]>
    </cmpScript>

    <cmpTabs>
        <cmpTabsItem caption="Блок 1 ">
            содержимое  блока1
        </cmpTabsItem>
        <cmpTabsItem caption="Блок 2 ">
            содержимое  блока2
        </cmpTabsItem>
        <cmpTabsItem caption="Блок 3 ">
            содержимое  блока3
        </cmpTabsItem>
    </cmpTabs>

</cmpForm>

