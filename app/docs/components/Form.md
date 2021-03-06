# Form

Компонент Form - Форма.
Любая форма должна начинаться и заканчиваться с тега компонента Form. Этот тег сообщает о том, что этот документ является ничем иным, как формой. Все компоненты, стили и другие компоненты относящиеся к данной форме прописываются внутри данного тега.

## Примеры синтаксиса

```xml
<div cmptype="Form" class="formBackground unitEditForm" oncreate="Form.onCreate();" icon="~Icon/gisgmp/22">
...
</div>
```

## Свойства компонента Form

|Название|Значение|Тип|Возможнные значения|get|set|
|---|---|---|---|---|---|
|caption|Отображаемый заголовок формы|string||\+|\+|
|class|Определяет класс стиля, назначенного данной форме|string||\-|\+|
|icon|Относительный путь до файла иконки, который будет отображаться в заголовке шапки.|string||\-|\+|
|oncreate|Метод, который срабатывает при открытии окна.|string||\-|\+|
|onshow|Метод, который срабатывает при отображении окна.|string||\-|\+|
|onclose|Метод, который срабатывает при закрытии окна.|string||\-|\+|
