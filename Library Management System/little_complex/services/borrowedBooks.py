from services.saveBooks import save
def borrowed(books):
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