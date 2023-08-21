from main import *

paper_book_1 = add_paper_book_document('Atlas Shrugged', 'Ayn Rand', 1957, ['''Philosophical fiction,
# # Libertarian science fiction, Mystery fiction, Romance novel'''], 1168)

books_id = books.insert_one(paper_book_1).inserted_id

print(books_id)
# как сделать поиск по айди если он возвращается после инсерт ван и все гг, то есть как обратиться к коллекции\документу
# чтобы достать оттуда айди??
