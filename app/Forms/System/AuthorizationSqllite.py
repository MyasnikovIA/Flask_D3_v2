import sqlite3  # SQLite

class ExecModule:
    def __init__(self, attrs):
        # Подключение через
        # DB = psycopg2.connect(database='flask_db', user='postgres', password='postgres', host='127.0.0.1', port=5432)
        attrs.get('globals')["DB"]['type'] = 'sqlite'
        attrs.get('globals')["DB"]['SQLconnect'] = sqlite3.connect("sqlite:///:memory:")
        attrs.get('globals')["DB"]['SQLconnect'] = sqlite3.connect("sqlite:////sqllite.db")
        attrs.get('globals')["DB"]['SQLconnect'].row_factory = sqlite3.Row
        attrs.get('globals')["DB"]['SQL'] = attrs.get('globals')["DB"]['SQLconnect'].cursor()
        # attrs.get('globals')["DB"]['SQLconnect'].close()



