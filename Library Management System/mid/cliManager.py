path = r"E:\CorePython\Library Management System\mid\Books_detail.txt"
def saveBooks(books):
    with open(path, "w") as file:
        file.write(str(books))
def mainMenuOutput(books):

    while True:
        print("\n")
        print("==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. View All")
        print("5. Search")
        print("6. Available Books")
        print("7. Borrowed Books")
        print("8. Back")
        print("==============================")
        choice = input("Enter your choice: ")
        if choice == "1":
            addBook(books)
        elif choice == "2":
            removeBook(books)
        elif choice == "3":
            updateBook(books)
        elif choice == "4":
            viewAll(books)
        elif choice == "5":
            search(books)
        elif choice == "6":
            availableBooks(books)
        elif choice == "7":
            borrowedBooks(books)
        elif choice == "8":
            back()
            break
        else:
            print("Invalid choice. Please try again.")


def addBook(books):
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
    saveBooks(books)
    print("Book added successfully!")

def removeBook(books):
    b_id = int(
        input("Enter the ID of the book to remove: ")
    )
    for book in books:
        if book["id"] == b_id:
            books.remove(book)
            saveBooks(books)
            print("Book removed successfully!")
            return
    print("Book not found.")

def updateBook(books):
    b_id=int(input("Enter the id of which book u want to update: "))
    for book in books:
        if book["id"] == b_id:
            title = input("Title: ")
            author = input("Author: ")
            publication_year = int(
                input("Publication Year: ")
            )
            book["title"] = title
            book["author"] = author
            book["publication_year"] = publication_year
            saveBooks(books)
            print("Book updated successfully!")
            return
        else:
            print("Book not found.")

def viewAll(books):
    print("Here is all the book avalible ")
    for book in books:
        print("------------------------------")
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Publication Year:", book["publication_year"])
        print("Available:", book["available"])
    print("------------------------------")

def search(books):
    b_id=int(input("Enter the id of which book u want to search: "))
    for book in books:
        if book["id"]==b_id:
            print("------------------------------")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Publication Year:", book["publication_year"])
            print("Available:", book["available"])
            print("------------------------------")
            return 

def availableBooks(books):
    print("Here is all the book avalible in library:- ")
    for book in books:
        if book["available"]:#"available": True createBooks.py(which means book is available) 
            print("------------------------------")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Publication Year:", book["publication_year"])
            print("Available:", book["available"])
            print("------------------------------")

def borrowedBooks(books):
    b_id=int(input("Enter the id of which book u want to Borrow: "))
    for book in books:
        if book["id"]==b_id:
            print("------------------------------")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Publication Year:", book["publication_year"])
            print("Available:", book["available"])
            print("------------------------------")
            book["available"] = False
            return

def back():
    print("Going back...")