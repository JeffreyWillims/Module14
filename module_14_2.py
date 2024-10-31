import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL    
    )
''')
cursor.execute('''DELETE FROM Users''') # Удаление Базы данных

for num in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
        (f"User{num}", f"example{num}@gmail.com", num * 10, 1000)
    )

for num in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE age = ?", (500, 10*num))

for user_id in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))

connection.execute("SELECT * FROM Users WHERE age!=60")

users = connection.execute("SELECT * FROM Users WHERE age != ?", (60,))


for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances/total_users)


connection.commit()
connection.close()