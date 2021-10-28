<div cmptype="Form">
    <cmpScript>
        <![CDATA[
            Form.onBtnTest2 = function() { }
        ]]>
    </cmpScript>

    <cmpToolbar  name="tlb_Ctrl" caption="Заголовок"  sttf="true" info="true" style="bottom: 20px;">
        <cmpToolbarItemGroup align="left">
            <cmpButton name="reports_Ctrl" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpPopupMenu name="p_reports_list_Ctrl">
                 <cmpPopupItem caption="Отчет 1"    std_icon="delete"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="группа">
                     <cmpPopupItem caption="Отчет 3"    std_icon="delete"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                 </cmpPopupItem>
            </cmpPopupMenu>
            <cmpButton name="reports_Ctrl"  caption="Отчеты2" width="50px" />
        </cmpToolbarItemGroup>
        <cmpToolbarItemGroup align="right">
            <cmpButton name="buttonSave" onclick="Form.onSave();" caption="Сохранить"/>
        </cmpToolbarItemGroup>
        <cmpToolbarItemGroup>
            <cmpButton name="buttonSave" onclick="Form.onSave();" caption="5345345"/>
        </cmpToolbarItemGroup>
    </cmpToolbar>

</div>
