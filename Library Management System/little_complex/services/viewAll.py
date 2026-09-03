from services.saveBooks import save
def view(books):
    print("Here is all the book avalible ")
    for book in books:
        print("------------------------------")
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Publication Year:", book["publication_year"])
        print("Available:", book["available"])
    print("------------------------------")