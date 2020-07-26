import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
cursor = conn.cursor()

### An example query
cursor.execute('SELECT * from test_table;')
#results = cursor.execute('SELECT * from test_table;').fetchone()
#print(results)

### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()
#print(results)


########## Connect to SQLite3 DB for RG data ############

import sqlite3

sl_conn = sqlite3.connect("rpg_db.sqlite3")
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10')
print(characters)