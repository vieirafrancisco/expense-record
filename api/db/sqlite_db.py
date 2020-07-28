import sqlite3

class SqliteDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.db_path = 'rsc/db/database.db'
        self.conn = None
        self.is_connected = False

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.is_connected = True
        except Exception as e:
            raise e

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

    def create_table(self, table_name, attributes):
        attrs = ", ".join(attributes)
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({attrs});"
        self.execute_commit(sql)

    def select_all_from(self, table_name, attr_names):
        keys = ", ".join(attr_names)
        self.connect()
        cur = self.conn.cursor()
        cur.execute(f"SELECT {keys} FROM {table_name}")
        data = cur.fetchall()
        return data

db = SqliteDB()

if __name__ == '__main__':
    ## Create tables
    #create_tables(db)
    ...
