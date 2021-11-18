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

import cx_Oracle
from sqlalchemy import Table, Column, String, Numeric, Float, Boolean, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
import pandas as pd

# session = sessionmaker()()

DB = {'SQL': '', 'META': '', 'TABLE': {},'PD':pd}
DB['Type'] = {}
DB['Type']['String'] = String
DB['Type']['Numeric'] = Numeric
DB['Type']['Float'] = Float
DB['Type']['Boolean'] = Boolean
DB['Select'] = select
DB['Session'] = ""

try:
    if 'DatabaseName' in ConfigOptions and len(ConfigOptions['DatabaseName']) > 0:
        DB['SQL'] = create_engine(ConfigOptions['DatabaseName'], execution_options={"isolation_level": "SERIALIZABLE"})
        DB['META'] = MetaData(DB['SQL'])
        session = sessionmaker()()
        DB['Session'] = session(bind = DB['SQL'])
        DB['TABLE'] = {}
except:
    print("ошибка подключения к БД", ConfigOptions['DatabaseName'])
    DB = {'SQL': '', 'META': '', 'TABLE': {}}
