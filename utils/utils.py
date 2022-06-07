from flask import jsonify

def generate_response(code, message, book={}):
    if book != {}:
        return {'code': code, 'message': message, 'book': book}
    return ({'code': code, 'message': message})