path = r"E:\CorePython\Library Management System\little_complex\data\Books_detail.txt"
def save(books):
    with open(path, "w") as file:
        file.write(str(books))