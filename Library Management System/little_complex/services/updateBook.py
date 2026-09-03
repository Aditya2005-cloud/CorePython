from services.saveBooks import save
def update(books):
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
            save(books)
            print("Book updated successfully!")
            return
        else:
            print("Book not found.")