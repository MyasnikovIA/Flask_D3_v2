#import cx_Oracle
class ExecModule:
    def __init__(self, attrs):
        sessionId = attrs.get('globals').get('session').get('ID')
        DB_DICT = attrs['DB_DICT'][sessionId]
        # Авторизация Oracle
        # 'DatabaseName': 'oracle://dev:dev@127.0.0.1:1521/dev',
        #dsn_tns = cx_Oracle.makedsn('192.168.228.41', 1521, 'med2dev')
        #DB_DICT['oracle']['SQLconnect'] = cx_Oracle.connect(attrs.get('DBLogin'), attrs.get('DBPassword'), dsn_tns)
        #DB_DICT['oracle']['SQL'] = DB_DICT['oracle']['SQLconnect'].cursor()



