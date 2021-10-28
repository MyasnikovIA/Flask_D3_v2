# Expander
Компонент Expander разкрывающийся блок
Раскрытие блока производится после нажатия на текст заголовка 
## Примеры синтаксиса

|Название|Значение|Тип|Возможные значения|
|---|---|---|---|
|height|высота компонента в раскрытом состоянии|string|число height="50" интерпретируется как 50px|
|caption|Отображаемое значение|string|Текст  заголовка|
|show|Признак показывать блок в раскрытом состоянии|string| Можно не указывать; show="false";  show="true"; |
|img| Ссылка на картинку (url)|string| Можно не указывать; картинка должна  иметь размеры width:10px height:25px |
|style|css-стиль компонента|string|   |
|path|Путь к форме, которая будет помещена в контейнер|string|   |

```xml
    
   <cmpExpander height="200px" show="false" caption="Заголовок" img="Components/Expander/images/arrow.png">
       <cmpButton caption="Содержимое разворачивающегося блока"/>
   </cmpExpander>

```

 

```xml
   <cmpExpander height="200px" show="false" caption="Заголовок" img="Components/Expander/images/arrow.png" path="Tutorial/main" >
       <cmpButton caption="Содержимое разворачивающегося блока"/>
   </cmpExpander>
```