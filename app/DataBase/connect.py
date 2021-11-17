from Etc.conf import ConfigOptions
from app import pd,psql

# 'DatabaseName': 'sqlite:////sqllite.db',
# 'DatabaseName': 'postgres://postgres:postgres@127.0.0.1:5432/flask_db',
# 'DatabaseName': 'oracle://dev:dev@127.0.0.1:5432/flask_db',
# 'DatabaseName': 'mysql+pymysql://admin:12345678@192.168.1.20:5155/myDB',

SQL = None
SQLconnect = None
try:
    if 'DatabaseName' in ConfigOptions and len(ConfigOptions['DatabaseName'])>0:
        DatabaseName = ConfigOptions['DatabaseName']
        DatabaseName = DatabaseName[DatabaseName.find("://") + 3:]
        if ":" in DatabaseName:
            userName = DatabaseName[:DatabaseName.find(":")]
            DatabaseName = DatabaseName[DatabaseName.find(":")+1:]
            userPass = DatabaseName[:DatabaseName.find("@")]
            DatabaseName = DatabaseName[DatabaseName.find("@") + 1:]
            ip = DatabaseName[:DatabaseName.find(":")]
            DatabaseName = DatabaseName[DatabaseName.find(":") + 1:]
            port = int(DatabaseName[:DatabaseName.find("/")])
            DatabaseName = DatabaseName[DatabaseName.find("/") + 1:]
            SID = DatabaseName

        if ConfigOptions['DatabaseName'].split(":")[0] == 'postgres':
            import psycopg2   # PostgreSQL
            SQLconnect = psycopg2.connect(database=SID, user=userName, password=userPass, host=ip, port=port)
            SQL = SQLconnect.cursor()
            # SQL.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, login VARCHAR(64), password VARCHAR(64))")
            # SQLconnect.commit()
            # SQLconnect.close()

        if ConfigOptions['DatabaseName'].split(":")[0] == 'sqlite':
            import sqlite3  # SQLite
            SQLconnect = sqlite3.connect(ConfigOptions['DatabaseName'][ConfigOptions['DatabaseName'].find(":///") + 4:])
            SQLconnect.row_factory = sqlite3.Row
            SQL = SQLconnect.cursor()
            # SQLconnect.close()

        if ConfigOptions['DatabaseName'].split(":")[0] == 'oracle':
            import cx_Oracle
            SQLconnect = psycopg2.connect(database=SID, user=userName, password=userPass, host=ip, port=port)
            dsn_tns = cx_Oracle.makedsn(ip, port, SID)
            SQLconnect = cx_Oracle.connect(userName, userPass, dsn_tns)
            SQL = SQLconnect.cursor()

            SQL.execute('''select ID,FULLNAME from D_V_LPU''');
            for test in SQL:
                print(test)
            # ====================================================================
            #import pandas as pd
            #import pandas.io.sql as psql
            # получение данных с применением библиотеки  pandas
            #df1 = psql.read_sql('select ID,FULLNAME from D_V_LPU', con=connection)
            #print(df1.head(n=10))
            # ====================================================================


except :
    print("ошибка подключения к БД", ConfigOptions['DatabaseName'])
    SQL = None
    SQLconnect = None
