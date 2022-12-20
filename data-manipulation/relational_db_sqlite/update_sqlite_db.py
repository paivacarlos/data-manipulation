import sqlite3

conn = sqlite3.connect('utils_db/sell.db')
cur = conn.cursor()

def update_value_register_to(current_value, update_value):
    cur.execute(f"UPDATE products SET value = {update_value} WHERE value = {current_value}")
    conn.commit()

update_value_register_to(90.00, 89.99)


cur.close()
conn.close()