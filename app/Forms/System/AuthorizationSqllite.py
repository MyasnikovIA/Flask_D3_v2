import sqlite3  # SQLite

class ExecModule:
    def __init__(self, attrs):
        # Подключение SQLite
        sessionId = attrs.get('globals').get('session').get('ID')
        DB_DICT = attrs['DB_DICT'][sessionId]
        DB_DICT['sqlite']['SQLconnect'] = sqlite3.connect("sqlite:///:memory:")
        # DB_DICT['sqlite']['SQLconnect'] = sqlite3.connect("sqlite:////sqllite.db")
        DB_DICT['oracle']['SQLconnect'].row_factory = sqlite3.Row
        DB_DICT['sqlite']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()
        # attrs.get('globals')["DB"]['SQLconnect'].close()



