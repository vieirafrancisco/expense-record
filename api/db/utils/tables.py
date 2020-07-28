import os
import json

TABLES_JSON_PATH = os.path.join("rsc", "sql", "tables.json")

def create_tables(db):
    with open(TABLES_JSON_PATH, 'r') as f:
        tables = json.load(f)
    for table_name, values in tables.items():
        db.create_table(table_name, values)