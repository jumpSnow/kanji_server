import sqlite3
conn = sqlite3.connect('ex1')

c = conn.cursor()

c.execute('''SELECT kanji FROM kanji''')
# c.execute('''.schema kanji''')
print(c.fetchall())
conn.commit()

