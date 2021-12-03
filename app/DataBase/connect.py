from Etc.conf import ConfigOptions

# https://www.pythonsheets.com/notes/python-sqlalchemy.html
# ConfigOptions['DatabaseName'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask_db'

# ===============================================================================
# Подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI.
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")

# Подключение к серверу MySQL по ip 23.92.23.113 с использованием mysql-python DBAPI.
# engine = create_engine("mysql+mysqldb://root:pass@23.92.23.113/mydb")

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
# engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")

# Подключение к серверу Oracle на локальном хосте с помощью cx-Oracle DBAPI.
# engine = create_engine("oracle+cx_oracle://root:pass@localhost/mydb")

# Подключение к MSSQL серверу на localhost с помощью PyODBC DBAPI.
# engine = create_engine("oracle+pyodbc://root:pass@localhost/mydb")

# Подключение к sqlite
# engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('sqlite:///sqlite3.db')  # используя относительный путь
# engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь
# ===============================================================================

import pandas as pd

# session = sessionmaker()()

DB = {'SQL': '', 'SQLconnect': '', 'META': '', 'TABLE': {}, 'PD': pd}
DB['Type'] = {}

try:
    if 'DatabaseName' in ConfigOptions and len(ConfigOptions['DatabaseName']) > 0:
        DatabaseName = ConfigOptions['DatabaseName']
        DatabaseName = DatabaseName[DatabaseName.find("://") + 3:]
        if ":" in DatabaseName:
            userName = DatabaseName[:DatabaseName.find(":")]
            DatabaseName = DatabaseName[DatabaseName.find(":") + 1:]
            userPass = DatabaseName[:DatabaseName.find("@")]
            DatabaseName = DatabaseName[DatabaseName.find("@") + 1:]
            ip = DatabaseName[:DatabaseName.find(":")]
            DatabaseName = DatabaseName[DatabaseName.find(":") + 1:]
            port = int(DatabaseName[:DatabaseName.find("/")])
            DatabaseName = DatabaseName[DatabaseName.find("/") + 1:]
            SID = DatabaseName

        if 'postgresql' in ConfigOptions['DatabaseName'].split(":")[0]:
            DB['type'] = 'postgres'
            import psycopg2  # PostgreSQL
            DB['SQLconnect'] = psycopg2.connect(database=SID, user=userName, password=userPass, host=ip, port=port)
            DB['SQLconnect'].autocommit = True
            DB['SQL'] = DB['SQLconnect'].cursor()
            DB['Type']['String'] = psycopg2.STRING
            DB['Type']['Number'] = psycopg2.NUMBER
            # SQL.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, login VARCHAR(64), password VARCHAR(64))")
            # SQLconnect.commit()
            # SQLconnect.close()

        if ConfigOptions['DatabaseName'].split(":")[0] == 'sqlite':
            # https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
            DB['type'] = 'sqlite'
            import sqlite3  # SQLite
            DB['SQLconnect'] = sqlite3.connect(
                ConfigOptions['DatabaseName'][ConfigOptions['DatabaseName'].find(":///") + 4:])
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
            # SQL.execute('''select ID,FULLNAME from D_V_LPU''');
            # for test in SQL:
            #    print(test)
            # ====================================================================
            # import pandas as pd
            # import pandas.io.sql as psql
            # получение данных с применением библиотеки  pandas
            # df1 = psql.read_sql('select ID,FULLNAME from D_V_LPU', con=connection)
            # print(df1.head(n=10))
            # ====================================================================

        # DB['SQL'] = create_engine(ConfigOptions['DatabaseName'], execution_options={"isolation_level": "SERIALIZABLE"})
        # DB['META'] = MetaData(DB['SQL'])
        # session = sessionmaker()()
        # DB['Session'] = session(bind = DB['SQL'])
        # DB['TABLE'] = {}
except:
    print("ошибка подключения к БД", ConfigOptions['DatabaseName'])
    DB = {'SQL': '', 'SQLconnect': '', 'META': '', 'TABLE': {}}
