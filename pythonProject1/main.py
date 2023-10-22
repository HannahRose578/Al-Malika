import requests
import json

headers = {'content-type': 'application/json'}

# GET all books
result = requests.get('http://127.0.0.1:5000/books', headers=headers)
print(result.json())

# Specific get request by genre
def get_books_by_genre(genre):
    genre_result = requests.get(
        f'http://127.0.0.1:5000/books/genre/{genre}',
        headers={'content-type': 'application/json'}
    )
    print(genre_result.json())
    return genre_result.json()

# POST REQUEST
def add_new_book(title, author, publication_year, isbn, genre):
    new_book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "isbn": isbn,
        "genre": genre
    }
    result = requests.post('http://127.0.0.1:5000/books', headers=headers, data=json.dumps(new_book))
    print(result.json())
    return result.json()

# PUT REQUEST
def update_genre(isbn, genre):
    updated_genre = {
        "genre": genre,
        "isbn": isbn
    }
    result = requests.put(f'http://127.0.0.1:5000/books/{isbn}', headers=headers, data=json.dumps(updated_genre))
    print(result.json())
    return result.json()

def run():
    print('############################')
    print('Hello, welcome to our bookclub')
    print('############################')
    print()
    get_book_list = input('Would you like to see what books we have been reading (y/n)?: ')
    if get_book_list.lower() == 'y':
        result = requests.get('http://127.0.0.1:5000/books', headers=headers)
        pretty_result = json.dumps(result.json(), indent=4)
        print(pretty_result)
    else:
        print('Maybe another time!')

if __name__ == '__main__':
    run()
