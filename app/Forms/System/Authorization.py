import psycopg2
#import cx_Oracle
import sqlite3

class ExecModule:
    def __init__(self, attrs):
        sessionId = attrs.get('globals').get('session').get('ID')
        DB_DICT = attrs['DB_DICT'][sessionId]
        # Авторизация Oracle
        # 'DatabaseName': 'oracle://dev:dev@127.0.0.1:1521/dev',
        #dsn_tns = cx_Oracle.makedsn('192.168.228.41', 1521, 'med2dev')
        #DB_DICT['oracle']['SQLconnect'] = cx_Oracle.connect(attrs.get('DBLogin'), attrs.get('DBPassword'), dsn_tns)
        #DB_DICT['oracle']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()

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



