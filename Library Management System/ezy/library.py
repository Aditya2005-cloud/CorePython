books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publication_year": 1988,
        "available": True
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "available": True
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "available": True
    },
    {
        "id": 4,
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "available": True
    },
    {
        "id": 5,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "available": True
    }
]


def show_books(books):

    if not books:
        print("No books available.")
        return

    for book in books:

        status = "Available" if book["available"] else "Borrowed"

        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Year: {book['publication_year']} | "
            f"Status: {status}"
        )


def add_book(books):

    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(
        input("Publication Year: ")
    )

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")


def search_books(books):

    keyword = input(
        "Enter the title you want to search: "
    ).lower()

    found = False

    for book in books:

        if keyword in book["title"].lower():

            status = (
                "Available"
                if book["available"]
                else "Borrowed"
            )

            print(
                f"ID: {book['id']} | "
                f"Title: {book['title']} | "
                f"Author: {book['author']} | "
                f"Year: {book['publication_year']} | "
                f"Status: {status}"
            )

            found = True

    if not found:
        print("Book not found.")


def remove_book(books):

    book_id = int(
        input("Enter the ID of the book to remove: ")
    )

    for book in books:

        if book["id"] == book_id:# book["id"] insted of it we can do 

            if not book["available"]:
                print(
                    "You cannot remove a borrowed book."
                )
                return

            books.remove(book)

            print("Book removed successfully!")
            return

    print("Book not found.")


def borrow_book(books):

    book_id = int(
        input("Enter the ID of the book to borrow: ")
    )

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:
                print(
                    "Sorry, this book is already borrowed."
                )
                return

            book["available"] = False

            print(
                f"You have borrowed "
                f"{book['title']} by {book['author']}."
            )

            return

    print("Book not found.")


def return_book(books):

    book_id = int(
        input("Enter the ID of the book to return: ")
    )

    for book in books:

        if book["id"] == book_id:

            if book["available"]:
                print(
                    "This book is not currently borrowed."
                )
                return

            book["available"] = True

            print(
                f"You have returned "
                f"{book['title']} by {book['author']}."
            )

            return

    print("Book not found.")


def main():

    while True:

        print("\n")
        print("==============================")
        print("       LIBRARY MANAGER")
        print("==============================")
        print("1. Show Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":

            show_books(books)

        elif choice == "2":

            add_book(books)

        elif choice == "3":

            search_books(books)

        elif choice == "4":

            borrow_book(books)

        elif choice == "5":

            return_book(books)

        elif choice == "6":

            remove_book(books)

        elif choice == "7":

            print("Goodbye!")
            break

        else:

            print("Invalid choice. Please try again.")


main()