# Layout
Компонент Layout представляет собой элемент формы контейнер в кото можно помещать элементы
Контейнер позволяет добавить разделительные элементы, для изменения размера окна 

## Примеры синтаксиса

```xml

 <cmpLayout name="MyLayout" >
       
        <cmpLayoutContainer  colspan="22"  style="height:25px">
              <cmpLabel caption="Верхняя панель"/>
        </cmpLayoutContainer>
     
        <!-- Разделительны элемент (горизонтальный) -->
        <cmpLayoutSplit orientation="horizon"/>
     
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
        <cmpLayoutSplit orientation="horizon" direction="bottom"/>
     
        <cmpLayoutContainer  colspan="25" >
            Нижняя панель
        </cmpLayoutContainer>
     
    </cmpLayout>

```

## Cвойство cmpLayoutSplit "orientation" 
Определяет  ориентацию разделительного элемента
```xml
 <cmpLayoutSplit orientation="horizon" />
```
|Название|Значение|
|---|---|
|vertical|Вертикальный разделитель панелей|
|horizon|Горизонтальный разделитель панелей|
Если параметр не установлен, тогда  `orientation = "vertical"`


## Cвойство cmpLayoutSplit "direction" 
```xml
 <cmpLayoutSplit direction="right" />
```
|Название|Значение|
|---|---|
|bottom|При смещении изменяется размер нижнего блока |
|left|При смещении изменяется размер левого блока |
|top|При смещении изменяется размер верхнего блока |
|right|При смещении изменяется размер правого блока |

Если параметр не установлен `direction` атребут и `orientation = "vertical"` тогда значение по умолчанию `direction="left"`
Если параметр не установлен `direction` атребут и `orientation = "horizon"` тогда значение по умолчанию `direction="top"`


## Cвойство cmpLayoutContainer "caption" 
```xml
 <cmpLayoutContainer caption="Заголовок панели" />
```
Произвольный текст
