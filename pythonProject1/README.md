# QUEENS Book Club API :books:

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
- MySQL

Any other dependencies will be automatically installed 

## Configuration

1. **Create a MySQL Database**: Execute the SQL script provided in `sql_script.sql` to create the `BookClub` database and the `Books` table.

2. **Configure Database Connection**:

   - Run the following code in MySQL to generate a user:

*CREATE USER 'almalika'@'localhost' IDENTIFIED BY 'cfg2023';
GRANT ALL PRIVILEGES ON *.* TO 'almalika'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;*

- Open `config.py` and replace the placeholders with your MySQL database details:

   ```python
   db_config = {
       'host': 'local host',
       'user': 'almalika',
       'password': 'cfg2023',
       'db': 'BookClub',
   }

## Running the API

To start the Flask application, run the following command:

*python app.py*

If it doesn't detect a config file for the DB Login it will ask the user for their DB login information and automatically creates the config.py file for them.

Once the API has fully loaded it will automatically open a new window for our 'client', a small cli app to interact wtih the endpoints

## API Endpoints

- **GET /books:** Get a list of all books.
- **PUT /books/<int:book_id>:** Change a book's author and title via its ID
- **GET /random_book:** Gets a random book.
- **POST /books:** Add a new book.
- **GET /books/genre:**  Retrieves and returns a list of all unique genres present in the database.

## Client Interaction

You can interact with the API using the provided `main.py` script. The updated `main.py` script allows you to perform the following actions:

1. **Get All Books**: Retrieve a list of all books in the database.

2. **Add a New Book**: Add a new book to the database. You will be prompted to enter the title and author of the book.

3. **Update a Book**: Update the title and author of an existing book. You will be prompted to enter the book ID, new title, and new author.

4. **Get a Random Book**: Retrieve a random book from the database.

5. **Get All Unique Genres**: Retrieve a list of all unique book genres in the database.

## Example Usage

When you run *main.py*, you will have 5 options (see above). Follow the prompts and make your selection. The client script will make requests to the API and display the results, allowing you to interact with the book database.
