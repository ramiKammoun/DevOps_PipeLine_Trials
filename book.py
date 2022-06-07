import sqlite3
from create_db import connect_to_db, create_db_table
from utils.utils import generate_response

def insert_book(book):
    inserted_book = {}
    try:
        conn = connect_to_db('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, numbers) VALUES (?, ?, ?)", (book['title'], book['author'], book['numbers']) )
        conn.commit()
        inserted_book = get_book_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()
    if (inserted_book != {}):
        return (generate_response(200, 'book added Successefully',inserted_book))
    else:
        return (generate_response(404, 'Could Not add book'))



def get_books():
    books = []
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()

        for i in rows:
            book = {}
            book["book_id"] = i["book_id"]
            book["title"] = i["title"]
            book["author"] = i["author"]
            book["numbers"] = i["numbers"]
            books.append(book)

    except:
        books = []

    return books


def get_book_by_id(book_id):
    book = {}
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        row = cur.fetchone()

        book["book_id"] = row["book_id"]
        book["title"] = row["title"]
        book["author"] = row["author"]
        book["numbers"] = row["numbers"]
    except:
        book = {}
    if book == {}:
        return (generate_response(404, 'book not found'))
    else:
        return book

def get_book_by_id2(book_id):
    book = {}
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        row = cur.fetchone()

        book["book_id"] = row["book_id"]
        book["title"] = row["title"]
        book["author"] = row["author"]
        book["numbers"] = row["numbers"]
    except:
        book = {}
    return book

def update_book(book):
    updated_book = {}
    try:
        conn = connect_to_db('database.db')
        cur = conn.cursor()
        cur.execute("UPDATE books SET title = ?, author = ?, numbers = ? WHERE book_id =?", (book["title"], book["author"], book["numbers"], book["book_id"],))
        conn.commit()
        updated_book = get_book_by_id(book["book_id"])

    except:
        conn.rollback()
        updated_book = {}
    finally:
        conn.close()
    if book == {}:
        return (generate_response(404, 'book not found'))
    else:
        return (generate_response(200, 'book Updated Successefully',updated_book))


def delete_book(book_id):
    message = {}
    message2 = {}
    try:
        
        conn = connect_to_db('database.db')
        usr = get_book_by_id2(book_id)
        conn.execute("DELETE from books WHERE book_id = ?", (book_id,))
        conn.commit()
        message["status"] = "book deleted successfully"
        message["code"] = 201
    except:
        conn.rollback()           
        print(message2)
    finally:
        conn.close()
    if (usr=={}):
        message["status"] = "Cannot delete book: book does not exist"
        message["code"] = 404    

    return message