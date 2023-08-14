from sqlite3 import connect

connection = connect('sqlite3.db')
cursor = connection.cursor()

# cursor.execute('''
#     CREATE TABLE persons(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name VARCHAR(20) NOT NULL,
#     last_name VARCHAR(20) NOT NULL,
#     sex VARCHAR(6),
#     age INTEGER
#     );
# ''')
#
# cursor.execute('''
#     CREATE TABLE students(
#     id INTEGER,
#     person_id INTEGER PRIMARY KEY,
#     course INTEGER NOT NULL,
#     FOREIGN KEY (person_id) REFERENCES persons(id)
#     );
# ''')
#
# cursor.execute('''
#     CREATE TABLE marks(
#     id INTEGER,
#     student_id INTEGER,
#     math INTEGER,
#     literature INTEGER,
#     chemistry INTEGER,
#     FOREIGN KEY (student_id) REFERENCES students(person_id)
#     );
# ''')

# persons = [(1, 'Denero', 'Cvach', 'male', 22), (2, 'Sashka', 'Ciba', 'male', 22)]
# cursor.execute('''
#     INSERT INTO persons (id, first_name, last_name, sex, age) VALUES (?, ?, ?, ?, ?)
#     ''', (1, 'Denero', 'Cvach', 'male', 22))
# connection.commit()

# cursor.execute('''
#     INSERT INTO persons (id, first_name, last_name, sex, age) VALUES (?, ?, ?, ?, ?)
#     ''', (2, 'Sashka', 'Ciba', 'male', 22))
# connection.commit()

# cursor.execute('''
#     INSERT INTO students (id, person_id, course) VALUES (?, ?, ?)
#     ''', (1, 1, 4))
# connection.commit()

# cursor.execute('''
#     INSERT INTO students (id, person_id, course) VALUES (?, ?, ?)
#     ''', (2, 2, 3))
# connection.commit()

# cursor.execute('''
#     INSERT INTO marks (id, student_id, math, literature, chemistry) VALUES (?, ?, ?, ?, ?)
#     ''', (1, 1, 10, 10, 10))
# cursor.execute('''
#     INSERT INTO marks (id, student_id, math, literature, chemistry) VALUES (?, ?, ?, ?, ?)
#     ''', (2, 2, 4, 5, 6))
# connection.commit()

# cursor.execute('SELECT * FROM persons')
# data = cursor.fetchall()
# for persons in data:
#     print(*persons)
#
# cursor.execute('SELECT first_name FROM persons')
# data = cursor.fetchone()
# print(*data)
#
# cursor.execute('SELECT last_name FROM persons')
# data = cursor.fetchall()
# for persons in data:
#     print(*persons)

sql = ('''
    SELECT *
    FROM persons
    INNER JOIN students
    ON persons.id = students.id
''')
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
