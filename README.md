# Flask_D3_v2
Трансляция фреймворка D3 от компании Bars-груп с PHP на Python(вариант2)

```

app\app.py - Скрипт сервера Flask (точка запуска проекта)
app\getform.py - Парсер Frm в HTML
app\Etc\conf.py - Распологается словарь с настройками проекта
app\Components - Содержит описание компонентов, стилей и библиотек для работы с этими компонентами
app\Forms      - Собержит формы для преобразования парсером
app\UserForms  - Содержит фрагменты XML для переопределения основных форм
app\db.shelve.dat - (создается при старте сервера) - Глобальный справочник в формате "ключ/значение"

app\requirements.txt - содержит список подключаемых модулей, которые необходимо инсталировать
------------------------------------
pip install -r requirements.txt 
------------------------------------

build.bat - скрипт для сборки Docker контейнера с проектом
run.bat - скрипт для запуска собранного Docker контейнера с проектом
save_images.bat - скрипт для выгразки архива Docker контейнера
commit_images.bat - скрипт для фиксации состояния работающего  Docker контейнера

```


*D3extClient* <br/>
android\D3ExtClient\app\build\outputs\apk\debug\app-debug.apk - браузер клинт D3 под андроид


<img src="https://github.com/MyasnikovIA/Flask_D3_v2/blob/main/img/scr.png?raw=true"/>


<img src="https://github.com/MyasnikovIA/Flask_D3_v2/blob/main/img/scrAndroid.png?raw=true"/>

Команды для работы с докером
```
docker save -o F:\DockerProject\Flask_Python_3.6\Flask_001(13.10.2020).tar python3.6_flask:flask_001     - выгразить контейнер в файл 
docker load -i F:\DockerProject\Flask_Python_3.6\Flask_001(13.10.2020).tar

-------------------------------------------------------------
COMMIT IMAGE
-------------------------------------------------------------
docker ps
docker images
docker commit d02a9d321c4b python3.6_flask:flask_001
-------------------------------------------------------------
```