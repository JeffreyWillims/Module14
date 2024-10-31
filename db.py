import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL, 
age INTEGER
)
               ''')



cursor.execute("CREATE INDEX IF NOT EXISTS new_idx_email ON Users (email)")

for i in range(30):
    cursor.execute("INSERT INTO Users(username, email, age) VALUES(?, ?, ?)",(f'newuser{i}', f"{i}ex@gmail.com", '28'))

connection.commit()
connection.close()