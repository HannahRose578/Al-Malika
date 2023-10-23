from flask import Flask, jsonify, request
import db_utils

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (new_book['title'], new_book['author']))
    connection.commit()
    connection.close()
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.json
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s WHERE id=%s", (updated_book['title'], updated_book['author'], book_id))
    connection.commit()
    connection.close()
    return jsonify(updated_book)

@app.route('/random_book', methods=['GET'])
def get_random_book():
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books ORDER BY RAND() LIMIT 1")
    book = cursor.fetchone()
    connection.close()
    return jsonify(book)

if __name__ == '__main__':
    app.run(debug=True)
