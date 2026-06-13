books=[]
def add_book():
    book={
        "Book name":input("Enter book name: "),
        "Author name":input("Enter author name: ")
    }
    books.append(book)
def show_all_book():
    for book in books:
        print(f"Book name: {book['Book name']}")
def buy_book():
    book_name=input("Enter book name: ")
    if book_name in books:
        print("Book Bought successfully")
        books.remove(book_name)
    else:
        print("Book not found")
def main():
    while True:
        print("1. Add Book")
        print("2. Show Books")
        print("3. Buy Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_book()
        elif choice == "3":
            buy_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()