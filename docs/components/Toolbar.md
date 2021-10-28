# Toolbar
Верхний бар страницы

## Компонент ToolbarItemGroup

Блок .

## Примеры синтаксиса

```xml
    <cmpToolbar  name="tlb_Ctrl" caption="Заголовок"  sttf="true" info="true">
        <cmpToolbarItemGroup align="left">
            <!--  Контент -->
            <cmpButton name="reports_Ctrl" popupmenu="p_reports_list_Ctrl" caption="Отчеты"/>
            <cmpPopupMenu name="p_reports_list_Ctrl">
                 <cmpPopupItem caption="Отчет 1"    std_icon="delete"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="группа">
                     <cmpPopupItem caption="Отчет 3"    std_icon="delete"/>
                     <cmpPopupItem caption="Отчет 4"    std_icon="edit"/>
                 </cmpPopupItem>
            </cmpPopupMenu>
            <!--  ======== -->
        </cmpToolbarItemGroup>
        <cmpToolbarItemGroup align="right">
            <!--  Контент -->
            <cmpButton name="buttonSave" onclick="Form.onSave();" caption="Сохранить"/>
            <!--  ======== -->
        </cmpToolbarItemGroup>
    </cmpToolbar>
```


## Свойства компонента cmpToolbar

|Название|Значение|Тип|Возможные значения|
|---|---|---|---|
|caption|Заголовок|string||
|sttf| |string|"true"/"false"|
|info| |string|"true"/"false"|

## Свойства компонента cmpToolbarItemGroup

|Название|Значение|Тип|Возможные значения|
|---|---|---|---|
|align|ориентация|string|align="left" - прижать к леву <br> align="right" - прижать к праву|

## Примечание

Если в cmpToolbar указать "bottom" тогда элемент нарисуется снизу 
<br/>``<cmpToolbar  name="tlb_Ctrl" bottom="1">``  