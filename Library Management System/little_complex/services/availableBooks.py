from services.saveBooks import save
def available(books):
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