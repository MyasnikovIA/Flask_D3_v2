# PopupMenu

Контекстное меню, вызываемое правой кнопкой мыши на объекте (либо по кнопке справа у Gridа - подробнее в описании компонента Grid)

## Компонент PopupItem

Пункт контекстного меню.

## Примеры синтаксиса

```xml
<cmpPopupMenu  name="gisgmp_payments_default_popup" popupobject="gisgmp_payments_default" onpopup="Form.onPopupPayments();">
	<cmpPopupItem  name="PAYMENTS_popup_upd"	caption="Обновить" onclick="Form.Refresh();"/>
	<cmpPopupItem  name="PAYMENTS_popup_view"	caption="Просмотр" onclick="Form.ViewPayment();"/>
</cmpPopupMenu>
```


## Свойства компонента PopupMenu

|Название|Значение|Тип|Возможные значения|
|---|---|---|---|
|popupobject|объект, к которому привязано меню|string||
|join_menu|Основное к которому, будет привязан текущий компонент PopupMenu. Необязательный атрибут|string||
|onpopup|Функция, которая будет срабатывать перед показом контекстного меню|string||
|separator|Атрибут устанавливает   линию подчеркивания после пункта меню|string|"before" "after"|
|placeholder|Выводит текст-подсказку внутри PopupMenu, который исчезает при получении фокуса "cmpPopupItem" |string||


## Свойства компонента PopupItem

|Название|Значение|Тип|Возможные значения|
|---|---|---|---|
|caption|Заголовок пункта меню|string||

## Примечание

* Для задания меню для контролов или любого dom объекта необходимо указать атрибут popupmenu="имя меню".
* Для задания меню формы на корне формы указать атрибут menu="имя меню".
* Для добавления одного меню к другому нужно указать атрибут join_menu="имя меню"
