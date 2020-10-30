import sqlite3


conn = sqlite3.connect('stock.db')

c = conn.cursor()

c.execute("SELECT rowid,* from users")

print(c.fetchall())

conn.commit()

conn.close()
