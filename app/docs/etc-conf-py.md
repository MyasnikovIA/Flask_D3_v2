# Настройки Etc/conf.inc

## Описание файла

Основной настроечный файл веб-части.

Файл представляет из себя python скрипт, объявляющий объект ConfigOptions. Ключи объекта - название настройки. 

Значение опции в python скрипте можно получить с помощью функции ```get_option('НАЗВАНИЕ_НАСТРОЙКИ',ЗНАЧЕНИЕ_ПО_УМОЛЧАНИЮ);```
 
```python
global ConfigOptions
ConfigOptions = {
    'DBType': 'MIS',
    'Database': 'SqliteDatabase',
    'DatabaseName': '//XXX.XXX.XXX.XXX/meddev:shared',
    'OutCodePage': 'UTF-8',
    'FormEncoding': 'UTF8',
    'DatabaseCharset': 'UTF8',
    'debug': 1,
    'Extensions': {'path': 'Extensions/', 'only': ['mis']},
    'TempDir': 'temp/',
    'help_conf'  : 'Etc/help.py',
	'TempTalonsDir' : 'c:/SharedTalonsDir/',
    'fs_store_dir': f'../file_storage{os.sep}',
    'FilesDir': 'Files/',
    'XlsCharset': 'windows-1251',
    'Forms': '/Forms',
    'UserForms': '/UserForms',
    'Exec7z': '/usr/bin/7za',
    'ExecZip': '/usr/bin/zip',
    'zint': '/usr/local/bin/zint',
    'zint_options': '--direct',
    'Theme': 'bars',
    'design_mode': 0,
    'enabled_modules': [],
    'cache_maxage': 3600,  # client
    'cache_enabled': 0,
    'cache_type': 'server',  # client, server, both
    'cache_dir': 'temp/cache/',
    'cache_ttl': 60 * 60 * 3,  # server
    'session_cache': 1,
    'cookie_lifetime': 900,
	#Прочие настройки
	#..................................................#
}	
```

## Параметры

### Строка подключения к БД

```
 'DatabaseName': '//XXX.XXX.XXX.XXX/meddev:shared',
```

### Папка юзерформ проекта

```
'UserForms': '/UserForms/',
```

Путь к папке с юзерформами, переопределяется настройкой в конкретном ЛПУ и параметром адресной строки **f=UserForms**

### Уровень дебага

```
	'debug': 1,
```

Значение больше 0 включает вывод отладочной информации. На продакшн сервере рекомендуемой значение 0.
Переопределяется параметром адресной строки **debug=1**


### Настройка wkhtmltopdf (для печати PDF)

```
'wkhtmltopdf' => array(
    'binpath'   : '/opt/wkhtmltox/bin/', // путь до директории с исполняющими файлам программы
    'binfile'   : 'wkhtmltopdf', // имя исполняющего файла
    'binprefix' : 'env LANG=ru_RU.UTF-8' // 
),
```

### Настройка авторизации через ЕСИАиА

```
'esia_auth' : {
    'enabled' : True, // Статус, вкл.(True)/выкл.(False)
    'sysuser' : array('esia', 'XXXXXXXX'), // Пользователь под которым подключаться к системе, array('логин','пароль')
   },
```

### Апплет считывателя карт

```
'use_cardreader' : 1,
```

### Апплет сканера штрихкода

```
'use_scanner' : 1,
```

### Плагин "КриптоПро ЭЦП Browser plug-in"

```
'use_cryptopro' : 1,
```

### Плагин "Рутокен Плагин"

```
'use_rutoken' : 1,
```