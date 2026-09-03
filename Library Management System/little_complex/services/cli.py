from services.addBook import add
from services.removeBook import remove
from services.updateBook import update
from services.viewAll import view
from services.search import search_book
from services.availableBooks import available
from services.borrowedBooks import borrowed

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
            add(books)
        elif choice == "2":
            remove(books)
        elif choice == "3":
            update(books)
        elif choice == "4":
            view(books)
        elif choice == "5":
            search_book(books)
        elif choice == "6":
            available(books)
        elif choice == "7":
            borrowed(books)
        elif choice == "8":
            print("Going back...")
            break
        else:
            print("Invalid choice. Please try again.")