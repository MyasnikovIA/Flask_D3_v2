<div cmptype="Form" caption="" width="60%" height="60%">
    <cmpScript name="main_script">
        <![CDATA[
            Form.onCreate = function() {  }

            Form.onPopupPayments = function(coords, show) {
              console.log(coords, show);

            }
        ]]>
    </cmpScript>

    Нажмите правой кнопкоу по контролу
    <cmpEdit name="MENU" popupmenu="pMENU"/>
    <cmpPopupMenu name="pMENU" onpopup="Form.onPopupPayments(coords, show);">
        <cmpPopupItem caption="обновить" onclick="alert(1)" std_icon="upload"/>
        <cmpPopupItem caption="-"/>
        <cmpPopupItem caption="22222222222222222" onclick="alert(1) " std_icon="delete">
            <cmpPopupItem caption="*****************" onclick="alert(1)"/>
            <cmpPopupItem caption="00000000000000000" onclick="alert(1)"/>
        </cmpPopupItem>
        <cmpPopupItem caption="3333333333333333" onclick="alert(1)"/>
    </cmpPopupMenu>



        <cmpEdit name="myEdit" />
        <cmpPopupMenu  name="myPopUpMenu2" popupobject="myEdit" onpopup="Form.onPopupPayments(coords, show);">
            <cmpPopupItem  name="PAYMENTS_popup_upd1"	caption="Обновить1" onclick="Form.Refresh();"/>
            <cmpPopupItem  name="PAYMENTS_popup_upd2"	caption="Обновить1" onclick="Form.Refresh();"/>
            <cmpPopupItem  name="PAYMENTS_popup_upd3"	caption="Обновить1" onclick="Form.Refresh();"/>
        </cmpPopupMenu>

       <cmpPopupMenu  name="extends"  join_menu="myPopUpMenu2">
            <cmpPopupItem  name="PAYMENTS_popup_view1"	caption="Просмотр1" onclick="Form.ViewPayment();"/>
            <cmpPopupItem  name="PAYMENTS_popup_view2"	caption="Просмотр1" onclick="Form.ViewPayment();"/>
            <cmpPopupItem  name="PAYMENTS_popup_view3"	caption="Просмотр1" onclick="Form.ViewPayment();"/>
        </cmpPopupMenu>




</div>
