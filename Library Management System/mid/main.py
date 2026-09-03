import os

from createBook import createBooks, loadBooks
from cliManager import mainMenuOutput,updateBook_not_to_call

path = r"E:\CorePython\Library Management System\mid\Books_detail.txt"

if not os.path.exists(path):
    createBooks()
    print("Created the books txt file and populated it with some books.")
else:
    print("Book txt file already exists.")

books = loadBooks()
mainMenuOutput(books)