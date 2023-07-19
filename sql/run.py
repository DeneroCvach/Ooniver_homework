from sqlalchemy.orm import sessionmaker

from sqlachemy_orm_deklarativ import engine, LibraryPerson, Book

Session = sessionmaker(bind=engine)
session = Session()
user_1 = LibraryPerson('Denero', 'Cvach')
user_2 = LibraryPerson('Sashka', 'Ciba')
user_3 = LibraryPerson('Anya', 'Dmtr')
book_1 = Book('American Psycho', 'Bret Easton Ellis', user_1)
session.add_all([user_1, user_2, user_3, book_1])
session.commit()
