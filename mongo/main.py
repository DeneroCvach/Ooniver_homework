import datetime
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

db = client.super_db
books = db.books


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
        book_id = books.insert_one(book).inserted_id
    else:
        book_id = books.insert_many(book).inserted_id

    return book_id


def book_id_finder(book_id):
    id = books.find_one({"_id": ObjectId(book_id)})

    return id


def get_all_books():
    books_collection = books.find()
    books_list = [book for book in books_collection]

    return books_list


def get_books_by_author(author):
    book_collection = books.find({'author': author})
    book_list = [book for book in book_collection]

    return book_list


def delete_book_by_id(book_id):
    db.books.update_one({'_id': ObjectId(book_id)}, {'$set': {'is_deleted': True}})
