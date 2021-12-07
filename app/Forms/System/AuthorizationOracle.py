import cx_Oracle

class ExecModule:
    def __init__(self, attrs):
        # Авторизация Oracle
        attrs.get('globals')["DB"]['type'] = 'oracle'
        # 'DatabaseName': 'oracle://dev:def@192.168.228.41:1521/med2dev',
        dsn_tns = cx_Oracle.makedsn('192.168.228.41', 1521, 'med2dev')
        attrs.get('globals')["DB"]['SQLconnect'] = cx_Oracle.connect(attrs.get('DBLogin'), attrs.get('DBPassword'), dsn_tns)
        attrs.get('globals')["DB"]['SQL'] = attrs.get('globals')["DB"]['SQLconnect'].cursor()



