from Etc.conf import ConfigOptions

# 'DatabaseName': 'sqlite:////sqllite.db',
# 'DatabaseName': 'postgres://postgres:postgres@127.0.0.1:5432/flask_db',
# 'DatabaseName': 'oracle://dev:dev@127.0.0.1:5432/flask_db',
# 'DatabaseName': 'mysql+pymysql://admin:12345678@192.168.1.20:5155/myDB',
import cx_Oracle

DB = {'SQL' : '','SQLconnect' : '' ,'type':''}

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
            DB['type'] = 'postgres'
            import psycopg2   # PostgreSQL
            DB['SQLconnect'] = psycopg2.connect(database=SID, user=userName, password=userPass, host=ip, port=port)
            DB['SQL'] = DB['SQLconnect'].cursor()
            # SQL.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, login VARCHAR(64), password VARCHAR(64))")
            # SQLconnect.commit()
            # SQLconnect.close()

        if ConfigOptions['DatabaseName'].split(":")[0] == 'sqlite':
            DB['type'] = 'sqlite'
            import sqlite3  # SQLite
            DB['SQLconnect'] = sqlite3.connect(ConfigOptions['DatabaseName'][ConfigOptions['DatabaseName'].find(":///") + 4:])
            DB['SQLconnect'].row_factory = sqlite3.Row
            DB['SQL'] = DB['SQLconnect'].cursor()
            # DB['SQLconnect'].close()

        if ConfigOptions['DatabaseName'].split(":")[0] == 'oracle':
            DB['type'] = 'oracle'
            import cx_Oracle
            dsn_tns = cx_Oracle.makedsn(ip, port, SID)
            DB['SQLconnect'] = cx_Oracle.connect(userName, userPass, dsn_tns)
            DB['SQL'] = DB['SQLconnect'].cursor()
            # ====================================================================
            #SQL.execute('''select ID,FULLNAME from D_V_LPU''');
            #for test in SQL:
            #    print(test)
            # ====================================================================
            #import pandas as pd
            #import pandas.io.sql as psql
            # получение данных с применением библиотеки  pandas
            #df1 = psql.read_sql('select ID,FULLNAME from D_V_LPU', con=connection)
            #print(df1.head(n=10))
            # ====================================================================


except :
    print("ошибка подключения к БД", ConfigOptions['DatabaseName'])
    DB = {'SQL' : '','SQLconnect' : '' ,'type':''}
