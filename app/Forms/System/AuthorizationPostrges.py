import psycopg2

class ExecModule:
    def __init__(self, attrs):
        # Подключение через
        # DB = psycopg2.connect(database='flask_db', user='postgres', password='postgres', host='127.0.0.1', port=5432)
        sessionId = attrs.get('globals').get('session').get('ID')
        DB_DICT = attrs['DB_DICT'][sessionId]
        DB_DICT['postgre']['SQLconnect'] =  psycopg2.connect(database='flask_db', user=attrs.get('DBLogin').lower(),password=attrs.get('DBPassword'), host='127.0.0.1', port=5432)
        DB_DICT['postgre']['SQLconnect'].autocommit = True
        DB_DICT['postgre']['SQL'] = DB_DICT['postgre']['SQLconnect'].cursor()



