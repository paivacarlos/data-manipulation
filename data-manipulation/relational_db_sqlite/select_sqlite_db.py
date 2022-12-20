import sqlite3

conn = sqlite3.connect('utils_db/sell.db')
cur = conn.cursor()

def read_all_data():
    cur.execute("SELECT * FROM products")
    for line in cur.fetchall():
        print(line)

def read_register_more_than(value_to_search):
    cur.execute(f"SELECT * FROM products WHERE value > {value_to_search}")
    print("====================//=======================================")
    for line in cur.fetchall():
        print(line)

def read_colums(colum):
    print("==================//==================colum================")
    cur.execute("SELECT * FROM products")
    for line in cur.fetchall():
        print(line[colum])

read_all_data()
read_register_more_than(1080)
read_colums(2)

cur.close()
conn.close()