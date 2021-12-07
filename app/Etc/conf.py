import os,shelve

# ROOT_DIR = f"{Path(__file__).parent.parent}{os.sep}"

global ConfigOptions
ConfigOptions = {
    'DatabaseName': 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask_db',
    # 'DatabaseName': 'oracle://dev:def@192.168.228.41:1521/med2dev',
    # 'DatabaseName': '',
    # 'DatabaseName': 'sqlite:///:memory:',
    # 'DatabaseName': 'sqlite:////sqllite.db',
    #'DatabaseName': 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask_db',
    # 'DatabaseName': 'oracle+cx_oracle://dev:dev@192.168.0.1:1521/MyBD',
    # 'DatabaseName': 'mysql+pymysql://admin:12345678@192.168.1.20:5155/myDB',
    'OutCodePage': 'UTF-8',
    'FormEncoding': 'UTF8',
    'DatabaseCharset': 'UTF8',
    'debug': "0",
}

