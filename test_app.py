from app import create_app
import pytest
from create_db import create_db_table
import os
# @pytest.fixture(scope="session", autouse=True)
# # tmp_path_factory = default  fixture
# def create_test_database(tmp_path_factory):
#     # Temporary directory
#     tmp_dir = tmp_path_factory.mktemp("tmp")
#     database_filename = tmp_dir / "test_database.db"
#     create_db_table(database_filename)
#     # Envirement variable
#     os.environ["DATABASE_FILENAME"] = str(database_filename)

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app(__name__)
#     testing_client = flask_app.test_client(use_cookies=False)
#     context = flask_app.app_context()
#     context.push()
#     yield testing_client
#     context.pop()


# def test_api_add_book(test_client):
#     expected_status_code = 200
#     expected_message= "book added Successefully"
#     response = test_client.post('/api/books/add', json={
#         "title": "Conversations with friends",
#         "author": "Sally Rooney",
#         "numbers": "123456789",
#     })
#     assert expected_status_code == response.json['code']
#     assert expected_message == response.json['message']

# def test_api_add_book2(test_client):
#     expected_status_code = 200
#     expected_message= "book added Successefully"
#     expected_body_keys = ["book_id", "title", "author","numbers"]
#     response = test_client.post('/api/books/add', json={
#         "title": "Normal People",
#         "author": "Sally Rooney",
#         "numbers": "555555874",
#     })
#     assert expected_status_code == response.json['code']
#     assert expected_message == response.json['message']
#     assert set(expected_body_keys) == response.json["book"].keys()
#     assert int == type(response.json["book"]["book_id"])

# def test_api_add_book3(test_client):
#     expected_status_code = 200
#     expected_message= "book added Successefully"
#     expected_body_keys = ["book_id", "title", "author","numbers"]
#     response = test_client.post('/api/books/add', json={
#         "title": "They both die in the end",
#         "author": "colleen",
#         "numbers": "89463168",
#     })
#     assert expected_status_code == response.json['code']
#     assert expected_message == response.json['message']
#     assert set(expected_body_keys) == response.json["book"].keys()
#     assert int == type(response.json["book"]["book_id"])

# def test_get_all_books(test_client):
#     # Given
#     expected_response = [
#         {
#             "title": "Conversations with friends",
#             "author": "Sally Rooney",
#             "numbers": "123456789",
#             "book_id":1
#         },
#         {
#             "title": "Normal People",
#             "author": "Sally Rooney",
#             "numbers": "555555874",
#             "book_id":2
#         },
#         {
#             "title": "They both die in the end",
#             "author": "colleen",
#             "numbers": "89463168",
#             "book_id":3
#         }
#     ]
#     expected_status_code = 200

#     # When
#     response = test_client.get("/api/books")

#     # Then
#     assert expected_status_code == response.status_code
#     assert expected_response == response.json

# def test_delete_existing_book(test_client):
#     # Given
#     id_to_delete = 2
#     expected_body = {
#         "code": 201,
#         "status": "book deleted successfully"
#     }

#     # When
#     response = test_client.delete(f'/api/books/delete/{id_to_delete}')

#     # Then
#     assert expected_body == response.json

# def test_get_all_books_after_delete(test_client):
#     # Given
#     expected_response = [
#         {
#             "title": "Conversations with friends",
#             "author": "Sally Rooney",
#             "numbers": "123456789",
#             "book_id":1
#         },
#         {
#             "title": "They both die in the end",
#             "author": "colleen",
#             "numbers": "89463168",
#             "book_id":3
#         }
#     ]
#     expected_status_code = 200

#     # When
#     response = test_client.get("/api/books")

#     # Then
#     assert expected_status_code == response.status_code
#     assert expected_response == response.json

# def test_delete_not_existing_book(test_client):
#     # Given
#     id_to_delete = 100
#     expected_body = {
#         "code": 404,
#         "status": "Cannot delete book: book does not exist"
#     }   

#     # When
#     response = test_client.delete(f'/api/books/delete/{id_to_delete}')

#     # Then
#     assert expected_body == response.json