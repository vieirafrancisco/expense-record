import os
import subprocess
from urllib.parse import urlparse

# dev
DEBUG = False

# database
DB_NAME = "database.db"
DB_PATH = os.path.join("rsc", "db")
DB_FILE_PATH = os.path.join(DB_PATH, DB_NAME)
TABLES_JSON_PATH = os.path.join("rsc", "sql", "tables.json")

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    subprocess.check_output(["heroku", "config:get", "DATABASE_URL"]).decode().replace('\n', '')
)
parse = urlparse(DATABASE_URL)
POSTGRESQL_CREDENTIALS = {
    "host": parse.hostname,
    "database": parse.path[1:],
    "user": parse.username,
    "password": parse.password
}