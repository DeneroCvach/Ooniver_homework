from sqlite3 import connect
# создаем подключение
connection = connect('sqlite_test_pycharm.db')
# создаем курсор
cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE basket (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     fruit_id INTEGER,
#     quantity INTEGER ,
#     FOREIGN KEY (fruit_id) REFERENCES basket(id)
# );
# ''')
#
# cursor.execute('''
# INSERT INTO fruits (name) VALUES (?)
# ''', ('banana',))
# connection.commit()
# cursor.execute('''
# INSERT INTO fruits (name) VALUES (?, ?)
# ''', ('pineapple', 'cherry'))
# connection.commit()

# fruits = [(10, 'orange'), (32, 'melon'),]
# cursor.executemany('INSERT INTO fruits (id, name) VALUES (?, ?)', fruits)
# connection.commit()

# cursor.execute('SELECT * FROM fruits')
# result = cursor.fetchall()
# print(result)

# cursor.execute('SELECT * FROM fruits')
# result = cursor.fetchmany(3)
# for fruit in result:
#     print(*fruit)

cursor.execute('INSERT INTO basket (fruit_id, quantity) VALUES (1, 12)')
cursor.execute('INSERT INTO basket (fruit_id, quantity) VALUES (2, 2)')
cursor.execute('INSERT INTO basket (fruit_id, quantity) VALUES (32, 6)')
connection.commit()
