from flask import Flask, jsonify, request
from db_utils import connect_to_db, execute_query, close_connection

app = Flask(__name__)

# Return all books
@app.route('/books', methods=['GET'])
def get_books():
    connection = connect_to_db()
    query = "SELECT * FROM Books"
    books = execute_query(connection, query)
    close_connection(connection)
    return jsonify(books)

# Get books by genre
@app.route('/books/genre/<genre>', methods=['GET'])
def get_books_by_genre(genre):
    connection = connect_to_db()
    query = "SELECT * FROM Books WHERE genre = %s"
    params = (genre,)
    books = execute_query(connection, query, params)
    close_connection(connection)
    return jsonify(books)

# Adding a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    connection = connect_to_db()
    query = "INSERT INTO Books (title, author, publication_year, isbn, genre) VALUES (%s, %s, %s, %s, %s)"
    params = (new_book['title'], new_book['author'], new_book['publication_year'], new_book['isbn'], new_book['genre'])
    execute_query(connection, query, params)
    close_connection(connection)
    return jsonify(new_book)

# Updating the genre of a book
@app.route('/books/<isbn>', methods=['PUT'])
def update_genre(isbn):
    updated_genre = request.get_json()
    connection = connect_to_db()
    query = "UPDATE Books SET genre = %s WHERE isbn = %s"
    params = (updated_genre['genre'], isbn)
    execute_query(connection, query, params)
    close_connection(connection)
    return jsonify(updated_genre)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
