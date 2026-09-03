import os 

from modules.create_Books import createBooks, loadBooks
from services.cli import mainMenuOutput

path = r"E:\CorePython\Library Management System\little_complex\data\Books_detail.txt"

if not os.path.exists(path):
    createBooks()
    print("Created the books txt file and populated it with some books.")
else:
    print("Book txt file already is there.")

books = loadBooks()
mainMenuOutput(books)