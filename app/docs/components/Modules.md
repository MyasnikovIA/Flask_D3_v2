# Modules

Компонент Modules используется для получения результатов запуска Python скриптов



```python
# Forms/System/Authorization.py
class ExecModule:
    def __init__(self, attrs):
        sessionId = attrs.get('globals').get('session').get('ID')
        DB_DICT = attrs['DB_DICT'][sessionId]
        # Авторизация Oracle
        dsn_tns = cx_Oracle.makedsn('192.168.228.41', 1521, 'med2dev')
        DB_DICT['oracle']['SQLconnect'] = cx_Oracle.connect(attrs.get('DBLogin'), attrs.get('DBPassword'), dsn_tns)
        DB_DICT['oracle']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()

        # Авторизация Oracle
        DB_DICT['postgre']['SQLconnect'] =  psycopg2.connect(database='flask_db', user=attrs.get('DBLogin').lower(),password=attrs.get('DBPassword'), host='127.0.0.1', port=5432)
        DB_DICT['postgre']['SQLconnect'].autocommit = True
        DB_DICT['postgre']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()

        # Авторизация Sqlite
        DB_DICT['sqlite']['SQLconnect'] = sqlite3.connect("sqlite:///:memory:")
        # DB_DICT['sqlite']['SQLconnect'] = sqlite3.connect("sqlite:////sqllite.db")
        DB_DICT['oracle']['SQLconnect'].row_factory = sqlite3.Row
        DB_DICT['sqlite']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()
        pass


```
для обращения к Forms/System/Authorization.py с клиентской формы, необходимо описать переменные для вызова
```xml
    <cmpModule  name="Authorization" mode="post" module="System/Authorization">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
```
Запуск из JS
```xml
  executeModule('Authorization', function() {
    // JS скрипт который отработает после выполнения Python скрипта
  })
```


Запустить произвольный Класс в сказанном Python скрипте 
```python
# Forms\System\AuthorizationV2.py
class ExecModuleEny:
    def __init__(self):
        pass

    def test(self, attrs):
        print(attrs)
        attrs["sdfsdfsd"] = 1111
        return attrs
```
на форме... 
```xml
    <cmpModule  name="Authorization2" mode="post" module="System/AuthorizationV2:ExecModuleEny.test">
        <cmpModuleVar  get="DBPassword"   srctype="ctrl" src="DBPassword"   name="DBPassword"/>
        <cmpModuleVar  get="DBLogin"      srctype="ctrl" src="DBLogin"      name="DBLogin"/>
    </cmpModule>
   
```