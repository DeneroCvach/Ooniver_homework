from main import *

paper_book_1 = add_paper_book_document('Atlas Shrugged', 'Ayn Rand', 1957, ['''Philosophical fiction,
# # Libertarian science fiction, Mystery fiction, Romance novel'''], 1168)

audio_book_1 = add_audio_book_document('The Magus', 'John Fowles', 'Tom Adams',1965,
                                       ['Mystery fiction, Romance novel'], 200)

e_book_1 = add_electronic_book_document('Women','Charles Bukowski', 1978, ['''Novel, autobiographical novel,
 # # Dark humor'''], 1.6, 'pdf')


paper_book_id = books.insert_one(paper_book_1).inserted_id
audio_book_id = books.insert_one(audio_book_1).inserted_id
e_book_id = books.insert_one(e_book_1).inserted_id


if __name__ == '__main__':
    print(get_all_books())
    print(book_id_finder(paper_book_id))
    print(get_books_by_author('Atlas Shrugged'))
