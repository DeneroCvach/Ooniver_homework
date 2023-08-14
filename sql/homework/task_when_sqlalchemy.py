from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sqlalchemy.db', echo=True)
with engine.connect() as connection:
    #   create_table_query = '''
    #       CREATE TABLE persons(
    #       id INTEGER PRIMARY KEY AUTOINCREMENT,
    #       first_name VARCHAR(20) NOT NULL,
    #       last_name VARCHAR(20) NOT NULL,
    #       sex VARCHAR(6),
    #       age INTEGER
    #   );
    # '''
    #
    #   create_table_query = '''
    #       CREATE TABLE students(
    #       id INTEGER,
    #       person_id INTEGER PRIMARY KEY,
    #       course INTEGER NOT NULL,
    #       FOREIGN KEY (person_id) REFERENCES persons(id)
    #   );
    #   '''
    #   create_table_query = '''
    #       CREATE TABLE marks(
    #       id INTEGER,
    #       student_id INTEGER,
    #       math INTEGER,
    #       literature INTEGER,
    #       chemistry INTEGER,
    #       FOREIGN KEY (student_id) REFERENCES students(person_id)
    #   );
    #   '''
    #   query = text(create_table_query)
    #   connection.execute(query)

    # insert_person_into_table = '''
    # INSERT INTO persons (id, first_name, last_name, sex, age)
    # VALUES (:id, :first_name, :last_name, :sex, :age)
    # '''
    # query = text(insert_person_into_table).bindparams(
    #     id=2,
    #     first_name='Sashka',
    #     last_name='Ciba',
    #     sex='male',
    #     age=22
    # )
    # connection.execute(query)
    # connection.commit()

    # insert_into_table_students = '''
    # INSERT INTO students (id, person_id, course)
    # VALUES (:id, :person_id, :course)
    # '''
    # query = text(insert_into_table_students).bindparams(
    #     id=1,
    #     person_id=1,
    #     course=4
    # )
    # connection.execute(query)
    # connection.commit()
    insert_into_table_marks = '''
    INSERT INTO marks (id, student_id, math, literature, chemistry)
    VALUES (:id, :student_id, :math, :literature, :chemistry)
    '''
    query = text(insert_into_table_marks).bindparams(
        id=1,
        student_id=1,
        math=10,
        literature=8,
        chemistry=9
    )
    connection.execute(query)
    connection.commit()
