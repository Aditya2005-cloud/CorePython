import ast#ast is being used specifically to convert the text from your .txt file back into Python data.

path = r"E:\CorePython\Library Management System\mid\Books_detail.txt"

def createBooks():
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
        }
    ]
    with open(path, "w") as file:
        file.write(str(books))

def loadBooks():
    with open(path, "r") as file:
        books = ast.literal_eval(file.read())
    return books