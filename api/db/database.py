from abc import ABC, abstractmethod
import sqlite3

import psycopg2

from settings import HEROKU_DB

class Database(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.conn = None
        self.is_connected = False

    @abstractmethod
    def connect(self, database=None):
        ...

    @abstractmethod
    def create_table(self, table_name, attributes):
        ...

    def close(self):
        if self.is_connected:
            self.conn.close()
            self.is_connected = False

    def execute_commit(self, sql):
        self.connect()
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        self.close()

    def insert_into_table(self, table_name, attr_names, tuple_values):
        """
        Inserir uma tupla em uma tabela específica do banco
        """
        keys = ", ".join(attr_names)
        values = ""
        for value in tuple_values:
            if values:
                values += ", "
            values += f"'{str(value)}'"
        sql = f"""INSERT INTO {table_name} ({keys})
        VALUES ({values})
        """
        self.execute_commit(sql)

    def select_all_from(self, table_name, attr_names):
        attrs = ", ".join(attr_names)
        self.connect()
        cur = self.conn.cursor()
        cur.execute(f"SELECT {attrs} FROM {table_name}")
        data = cur.fetchall()
        return data

    def select_one_from(self, table_name, attr_names, where):
        attrs = ", ".join(attr_names)
        key, value = tuple(where.items())[0]
        value = f"'{value}'"
        self.connect()
        cur = self.conn.cursor()
        cur.execute(f"SELECT {attrs} FROM {table_name} WHERE {key} == {value}")
        data = cur.fetchone()
        return data

class SqliteDB(Database):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path

    def connect(self, database=sqlite3):
        try:
            self.conn = database.connect(self.db_path)
            self.is_connected = True
        except Exception as e:
            raise e

    def create_table(self, table_name, attributes):
        attrs = ", ".join(attributes)
        sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            {attrs});"""
        self.execute_commit(sql)

class PostgresDB(Database):
    def __init__(self, host, db_name, user, password):
        super().__init__()
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password

    def connect(self, database=psycopg2):
        try:
            self.conn = database.connect(
                host=self.host, 
                database=self.db_name, 
                user=self.user, 
                password=self.password
            )
            self.is_connected = True
        except Exception as e:
            raise e

    def create_table(self, table_name, attributes):
        attrs = ", ".join(attributes)
        sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            {attrs});"""
        self.execute_commit(sql)


if not HEROKU_DB:
    from settings import DB_FILE_PATH
    db = SqliteDB(DB_FILE_PATH)
else:
    from settings import POSTGRESQL_CREDENTIALS
    db = PostgresDB(
        POSTGRESQL_CREDENTIALS["host"],
        POSTGRESQL_CREDENTIALS["database"],
        POSTGRESQL_CREDENTIALS["user"],
        POSTGRESQL_CREDENTIALS["password"]
    )
