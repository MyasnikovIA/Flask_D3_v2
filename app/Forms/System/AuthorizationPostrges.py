import psycopg2

class ExecModule:
    def __init__(self, attrs):
        # Подключение через
        # DB = psycopg2.connect(database='flask_db', user='postgres', password='postgres', host='127.0.0.1', port=5432)
        attrs.get('globals')["DB"]['type'] = 'postgres'
        attrs.get('globals')["DB"]['SQLconnect'] = psycopg2.connect(database='flask_db', user=attrs.get('DBLogin').lower(),password=attrs.get('DBPassword'), host='127.0.0.1', port=5432)
        attrs.get('globals')["DB"]['SQLconnect'].autocommit = True
        attrs.get('globals')["DB"]['SQL'] = attrs.get('globals')["DB"]['SQLconnect'].cursor()



