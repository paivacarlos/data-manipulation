import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('utils_db/sell.db')
cur = conn.cursor()

def data_graphic():
    cur.execute("SELECT id, value FROM products")
    ids = []
    values = []
    data = cur.fetchall()
    for line in data:
        ids.append(line[0])
        values.append(line[1])

    plt.bar(ids, values)
    plt.show()

data_graphic()

cur.close()
conn.close()