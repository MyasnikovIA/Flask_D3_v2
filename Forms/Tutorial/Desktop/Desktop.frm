<div cmptype="Form" onshow="Form.onShowForm()" caption="Рабочий стол">
    <cmpScript>
        <![CDATA[
            Form.onShowForm = function() {
                let timerId = setTimeout(function tick() {
                    var today = new Date();
                    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
                    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                    var dateTime = date+' '+time;
                    setCaption("timeNew",dateTime);
                  timerId = setTimeout(tick, 1000);
                }, 1000);
            }
        ]]>
    </cmpScript>


  <!-- нижняя полоска с меню и временем -->
  <cmpToolbar  name="tlb_Ctrl" caption=""  sttf="true" info="true" bottom="1" >
    <cmpToolbarItemGroup align="left">
       <cmpButton name="reports_Ctrl" popupmenu="p_reports_list_Ctrl" caption="Пуск" width="50px" />
            <cmpPopupMenu name="p_reports_list_Ctrl">
                 <cmpPopupItem caption="Отчервапрвапрвапрвапрварат 1"    std_icon="delete"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="группа">
                     <cmpPopupItem caption="Отчет 3"    std_icon="delete"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="группа">
                       <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                       <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                       <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                       <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     </cmpPopupItem>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                 </cmpPopupItem>
            </cmpPopupMenu>
    </cmpToolbarItemGroup>
    <cmpToolbarItemGroup align="right">
        <cmpLabel name="timeNew" />
    </cmpToolbarItemGroup>
  </cmpToolbar>





<!--
    <cmpDesktop  name="tlb_Ctrl" caption="Заголовок"  sttf="true" info="true" style="bottom: 20px;">

    </cmpDesktop>
-->
</div>
