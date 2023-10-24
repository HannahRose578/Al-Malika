import requests
import json

BASE_URL = "http://localhost:5000"

def get_all_books():
    response = requests.get(f"{BASE_URL}/books")
    print("Get All Books:")
    print(json.dumps(response.json(), indent=4))

def add_new_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    new_book = {'title': title, 'author': author}
    response = requests.post(f"{BASE_URL}/books", json=new_book)
    print("Add a New Book:")
    print(json.dumps(response.json(), indent=4))

def update_book():
    book_id = input("Enter the book ID to update: ")
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")
    updated_book = {'title': title, 'author': author}
    response = requests.put(f"{BASE_URL}/books/{book_id}", json=updated_book)
    print("Update a Book:")
    print(json.dumps(response.json(), indent=4))

def get_random_book():
    response = requests.get(f"{BASE_URL}/random_book")
    print("Get a Random Book:")
    print(json.dumps(response.json(), indent=4))

def get_unique_genres():
    response = requests.get(f"{BASE_URL}/books/genre")
    print("All Unique Genres:")
    print(json.dumps(response.json(), indent=4))

while True:
    print("\nChoose an option:")
    print("1. Get All Books")
    print("2. Add a New Book")
    print("3. Update a Book")
    print("4. Get a Random Book")
    print("5. Get All Unique Genres")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        get_all_books()
    elif choice == '2':
        add_new_book()
    elif choice == '3':
        update_book()
    elif choice == '4':
        get_random_book()
    elif choice == '5':
        get_unique_genres()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
