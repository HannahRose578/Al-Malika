import os
import subprocess
from platform import system
from flask import Flask, jsonify, request

app = Flask(__name__)

# Function to create a config.py file
def create_config_file():
    print("No config.py file found. Let's create one.")
    db_host = input("Enter your database host: ")
    db_user = input("Enter your database user: ")
    db_password = input("Enter your database password: ")
    db_name = input("Enter your database name: ")

    with open("config.py", "w") as f:
        f.write(f"DB_CONFIG = {{\n")
        f.write(f"    'host': '{db_host}',\n")
        f.write(f"    'user': '{db_user}',\n")
        f.write(f"    'password': '{db_password}',\n")
        f.write(f"    'database': '{db_name}'\n")
        f.write(f"}}\n")

    print("config.py has been created. Please restart the application.")

# Check if config.py exists
if not os.path.exists("config.py"):
    create_config_file()
    exit(1)  # Exit the application so the user can restart it


#Since db_utils relies on config we only import it after we know its there, even though an import so far down looks odd
import db_utils

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


# Return a list of all the genres
@app.route('/books/genre', methods=['GET'])
def get_genres():
    connection = db_utils.get_db_connection()
    cursor = connection.cursor()
    query = "SELECT DISTINCT genre FROM Books;"
    cursor.execute(query)
    genres = cursor.fetchall()
    connection.close()
    return jsonify(genres)

only_once = True

if __name__ == '__main__':
    if only_once:
        if system() == "Windows":
            subprocess.Popen("start cmd.exe /k python main.py", shell=True)
        only_once = False
    app.run(debug=True, use_reloader=False)
