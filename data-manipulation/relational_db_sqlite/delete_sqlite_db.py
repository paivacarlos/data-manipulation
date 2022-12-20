import sqlite3

conn = sqlite3.connect('utils_db/sell.db')
cur = conn.cursor()

def delete_register(id):
    cur.execute(f"DELETE FROM products WHERE id = {id}")
    conn.commit()

delete_register(5)

cur.close()
conn.close()