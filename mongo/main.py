import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.super_db
books = db.boooks


def add_paper_book_document(title, author, year_of_publishing, genre, pages):
    paper_book = {
        'title': title,
        'author': author,
        'year_of_publishing': year_of_publishing,
        'genre': genre,
        'pages': pages,
        'data': datetime.datetime.now(tz=datetime.timezone.utc)
    }

    return paper_book


def add_audio_book_document(title, author, voice_actor, year_of_publishing, genre, size):
    audio_book = {
        'title': title,
        'author': author,
        'voice_actor': voice_actor,
        'year_of_publishing': year_of_publishing,
        'genre': genre,
        'size': size,
        'data': datetime.datetime.now(tz=datetime.timezone.utc)
    }

    return audio_book


def add_electronic_book_document(title, author, year_of_publishing, genre, size, archive_format):
    e_book = {
        'title': title,
        'author': author,
        'year_of_publishing': year_of_publishing,
        'genre': genre,
        'size': size,
        'archive_format': archive_format,
        'data': datetime.datetime.now(tz=datetime.timezone.utc)
    }

    return e_book


def add_book_to_db(book):
    if type(book) is list:
        book_id = books.insert_many(book).inserted_id
    else:
        book_id = books.insert_one(book).inserted_id

    return book_id


def book_id_finder(book_id):
    id = books.find_one({"_id": book_id})

    return id

# print(post_1_id)
# print(posts.find())
# document = posts.find({"_id": post_1_id})
# posts = posts.find()
