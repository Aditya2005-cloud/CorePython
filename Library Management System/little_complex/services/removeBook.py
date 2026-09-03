from services.saveBooks import save

def remove(books):
    b_id = int(
        input("Enter the ID of the book to remove: ")
    )
    for book in books:
        if book["id"] == b_id:
            books.remove(book)
            save(books)
            print("Book removed successfully!")
            return
    print("Book not found.")