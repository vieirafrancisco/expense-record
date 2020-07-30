import os
import json

from db.sqlite_db import db
from settings import DB_NAME, DB_PATH, TABLES_JSON_PATH

def create_tables(db):
    with open(TABLES_JSON_PATH, 'r') as f:
        tables = json.load(f)
    for table_name, values in tables.items():
        db.create_table(table_name, values)

def setup_run():
    if DB_NAME not in os.listdir(DB_PATH):
        create_tables(db)
        print("Success on create the database!")
