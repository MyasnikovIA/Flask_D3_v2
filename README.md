# Flask_D3Ext_v2
Трансляция фреймворка D3 от компании Bars-груп с PHP на Python3.8(вариант2)

**Для чего эта разработка**
Разработка была сделана для расширения стандартной HTML компонентной базы.
<br/>Поведение пользовательских компонентов , которые будут использоватся в проекте описано 
<br/>в каталоке "app\Components"
<br/>При использовании компонентов название начинается со слова "cmp"
<br/>На пример, необходимо подключить компонент в HTML странице, описанный в каталоге "app\Components\Button"
<br/> тэг будет выглядить так ```<cmpButton caption="push my" onclick="alert('click')"/>```
<br/>__Html страница будет такой:__
```html
<html lang="en">
	<head>
		<link rel="stylesheet" type="text/css" href="./~d3theme"/>
		<script src="./~d3main"></script>
	</head>
	<body>
		<div>
			<cmpButton caption="push my" onclick="alert('click')"/>
		</div>
	</body>
</html>
```

**Примеры применения компонентов распологаются в каталоге "app\Forms\Tutorial"**


**Запуск платформы в Docker контейнере**
```
1) Скачать репозиторий локально;
2) Запустить Docker (авторизоватся);
3) Запустить скрипт для сборки Docker контейнера "build.bat"(подождать окончания сборки);
4) Запустите контейнер через скрипт "run.bat". Полсе запуска через 10 секунд откроется браузер 
   или перейти по адресу   http://127.0.0.1:9091/
```
<br>Развертывание  платформы в Docker:  https://youtu.be/IsNmCKiFTuY
<br>[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/IsNmCKiFTuY/0.jpg)](https://www.youtube.com/watch?v=IsNmCKiFTuY)
<br>
<br>

**Запуск платформы локально**
```
1) Скачать репозиторий локально;
2) Перейти в директорию платформы "\Flask_D3_v2\app"
3) В командной строке установить виртуальное окружение cmd:virtualenv env
4) Активировать виртуальное окружение cmd:env\Scripts\activate.bat
5) Установить зависимости проекта cmd:pip3 install -r requirements.txt
6) Запустить сервер cmd:python app.py 5001
    5001 - порт на котором запустился сервер
	Запустить браузер и перейти по адресу http://127.0.0.1:5001/
``` 
<br>Запуск платформы локально:  https://youtu.be/LV5cnsGonZU
<br>[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/LV5cnsGonZU/0.jpg)](https://www.youtube.com/watch?v=LV5cnsGonZU)
<br>
<br>


**Назначение файлов и директорий в проекте**
```
app\app.py - Скрипт сервера Flask (точка запуска проекта)
app\getform.py - Парсер Frm в HTML
app\Components - Содержит описание компонентов, стилей и библиотек для работы с этими компонентами
app\Forms      - Содержит формы для преобразования парсером
app\UserForms  - Содержит фрагменты XML для переопределения основных форм
app\requirements.txt - содержит список подключаемых модулей, которые необходимо инсталлировать
build.bat - скрипт для сборки Docker контейнера с проектом
run.bat - скрипт для запуска собранного Docker контейнера с проектом
save_images.bat - скрипт для выгрузки архива Docker контейнера
commit_images.bat - скрипт для фиксации состояния работающего  Docker контейнера


Вынрузить зависимости проекта
------------------------------------
pip install -r requirements.txt 
------------------------------------
```

**Возможности платформы** <br/>
```
Платформа работает на микрофреймворке Flask.
Основная логика конвертации XML документа в HTML верстку  реализовано в файле getform.py
Логика описана в процедурном стиле, и нуждается в оптимизации производительности. Данный продукт
написан в качестве визуализации концепции микросервесной распределенной архитектуре.     
 
1) Есть возможность одновременно подключатся к разным БД из списка (Oracle, PostgreSQL, Sqlite).
   подключений может быть не ограниченное количество. Каждое подключение имеет свой псевдоним,
   по которому  идет определения для какой БД был написан SQL запрос на форме (Action, DataSet)  
2) Есть возможность обращается к внешним серверам из браузера(в фоновом режиме).
   Пример:
             openD3Form('http://192.168.15.200:5000/index.html', true);  
  
3) Реализовано использование всех компонентов из каталога "Components" в HTML страницах
```

**Flask_D3_client (Android) --- в разработке!!!!** <br/>
android\Flask_D3_client\app\build\outputs\apk\debug\app-debug.apk - браузер клинт D3 под андроид

Если в JS коде присутствует объект  с именем Android значит в качестве браузера выступает **"D3extClient"** 

<img src="https://github.com/MyasnikovIA/Flask_D3_v2/blob/main/img/scr.png?raw=true"/>


<img src="https://github.com/MyasnikovIA/Flask_D3_v2/blob/main/img/scrAndroid.png?raw=true"/>

Команды для работы с докером
```
docker save -o F:\DockerProject\Flask_Python_3.8\Flask_001(13.10.2020).tar python3.6_flask:flask_001     - выгразить контейнер в файл 
docker load -i F:\DockerProject\Flask_Python_3.8\Flask_001(13.10.2020).tar

-------------------------------------------------------------
COMMIT IMAGE
-------------------------------------------------------------
docker ps
docker images
docker commit d02a9d321c4b python3.8_flask:flask_001
-------------------------------------------------------------
```
