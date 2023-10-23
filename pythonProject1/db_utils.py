import pymysql
from config import db_config
from pymysql import Error

# Create a database connection
def connect_to_db():
    try:
        db = pymysql.connect(**db_config
        )
    except Error as e:
        print(f"Error connecting to the database: {e}")
        db = None

# Function to get all books
def get_books():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        cursor.close()
        return [{'title': title, 'author': author, 'publication_year': year, 'isbn': isbn, 'genre': genre} for
                (title, author, year, isbn, genre) in books]
    except Error as e:
        print(f"Error getting books from the database: {e}")
        return []

# Function to search for books by title or author
def search_books(query):
    try:
        cursor = db.cursor()
        query = f"%{query}%"
        cursor.execute("SELECT * FROM Books WHERE title LIKE %s OR author LIKE %s", (query, query))
        books = cursor.fetchall()
        cursor.close()
        return [{'title': title, 'author': author, 'publication_year': year, 'isbn': isbn, 'genre': genre} for
                (title, author, year, isbn, genre) in books]
    except Error as e:
        print(f"Error searching for books: {e}")
        return []

# Function to add a new book
def add_book(title, author, publication_year, isbn, genre):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO Books (title, author, publication_year, isbn, genre) VALUES (%s, %s, %s, %s, %s)",
                       (title, author, publication_year, isbn, genre))
        db.commit()
        cursor.close()
        return {'title': title, 'author': author, 'publication_year': publication_year, 'isbn': isbn, 'genre': genre}
    except Error as e:
        print(f"Error adding a new book: {e}")
        return {}

# Close the database connection when done
def close_db_connection():
    if db:
        db.close()

# Call close_db_connection() when you're done using the database
# Example: close_db_connection()
