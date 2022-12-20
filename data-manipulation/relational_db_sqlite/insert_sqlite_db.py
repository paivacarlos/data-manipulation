import sqlite3
import random
import time
import datetime

conn = sqlite3.connect('utils_db/sell.db')
cur = conn.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS products('
                'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                'date TEXT,'
                'prod_name TEXT, '
                'value REAL)')

def data_insert():
    cur.execute("INSERT INTO products VALUES (9, '2022-06-02 11:10:00', 'Keyboard', 90)")
    conn.commit()

create_table()
data_insert()

#using variables to insert data
def data_insert_by_var():
    new_id = random.randrange(1000, 2000)
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_value = random.randrange(800, 1200)
    cur.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                (new_id, new_date, new_prod_name, new_value))
    conn.commit()

#creating values and insert in the db
for i in range(10):
    data_insert_by_var()
    time.sleep(1)

cur.close()
conn.close()
