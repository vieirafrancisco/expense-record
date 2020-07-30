import os

# dev
DEBUG = True

# database
DB_NAME = "database.db"
DB_PATH = os.path.join("rsc", "db")
DB_FILE_PATH = os.path.join(DB_PATH, DB_NAME)
TABLES_JSON_PATH = os.path.join("rsc", "sql", "tables.json")