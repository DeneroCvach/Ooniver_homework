from sqlalchemy import create_engine, text

eng = create_engine('sqlite:///library.db', echo=True)
with eng.connect() as connection:
    #     create_table_query = '''
    #         CREATE TABLE book (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             title VARCHAR NOT NULL,
    #             pages INTEGER NOT NULL,
    #             author VARCHAR,
    #             price FLOAT,
    #             release_year INTEGER
    #         )
    #     '''
    #     query = text(create_table_query)
    #     connection.execute(query)

    insert_book_into_table = '''
        INSERT INTO book (title, pages, author, price, release_year)
        VALUES (:title, :pages, :author, :price, :release_year)
    '''
    query = text(insert_book_into_table).bindparams(
        title='DeniskinyR',
        pages=200,
        author='Victor Dragunsky',
        price=10,
        release_year=1977
    )
    connection.execute(query)
    if input('yY -> ') in 'yY':
        connection.commit()
    else:
        connection.rollback()
