import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from create_db import create_db_table
from book import delete_book, insert_book, get_books, get_book_by_id, update_book
from utils.utils import generate_response
create_db_table('database.db')
def create_app(name):
    app = Flask(name)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route('/api/books', methods=['GET'])
    def api_get_books():
        return jsonify(get_books())

    @app.route('/api/books/<book_id>', methods=['GET'])
    def api_get_book(book_id):
        return (get_book_by_id(book_id))

    @app.route('/api/books/add',  methods = ['POST'])
    def api_add_book():
        book = request.get_json()
        if not book:
            return generate_response(400, 'Invalid payload.')
        return (insert_book(book))

    @app.route('/api/books/update',  methods = ['PUT'])
    def api_update_book():
        book = request.get_json()
        if not book:
            return generate_response(400, 'Invalid payload.')
        return (update_book(book))

    @app.route('/api/books/delete/<book_id>',  methods = ['DELETE'])
    def api_delete_book(book_id):
        return (delete_book(book_id))
    return app

if __name__ == "__main__":
        app = create_app(__name__)
        app.run()