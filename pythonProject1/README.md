# Book Club API :books:

## Table of Contents

- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Client Interaction](#client-interaction)
- [Example Usage](#example-usage)

---

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- MySQL
- `pymysql` library

## Configuration

1. **Create a MySQL Database**: Execute the SQL script provided in `sql_script.sql` to create the `BookClub` database and the `Books` table.

2. **Configure Database Connection**:

   - Run the following code in MySQL to generate a user:

*CREATE USER 'almalika'@'localhost' IDENTIFIED BY 'cfg2023';
GRANT ALL PRIVILEGES ON *.* TO 'almalika'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;*

- Open `config.py` and replace the placeholders with your MySQL database details:

   ```python
   sb_config = {
       'host': 'local host',
       'user': 'almalika',
       'password': 'cfg2023',
       'db': 'BookClub',
   }

## Running the API

To start the Flask application, run the following command:

*python app.py*

The API will be accessible at http://127.0.0.1:5000/.

## API Endpoints

- **GET /books:** Get a list of all books.
- **GET /books/genre/{genre}:** Get books by a specific genre.
- **GET /books/author:** Get books by authors whose names start with 'A'.
- **POST /books:** Add a new book.
- **PUT /books/{isbn}:** Update the genre of a book by ISBN.

## Client Interaction

You can interact with the API using the provided main.py script. To simulate interaction with the API, run the following command:
  
*python main.py*

## Example Usage

When you run *main.py*, you will have the option to view the list of books and make various requests to the API.
