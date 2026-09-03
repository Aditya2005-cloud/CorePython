from services.saveBooks import save
def add(books):
    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(input("Publication Year: "))
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "available": True
    }
    books.append(book)
    save(books)
    print("Book added successfully!")