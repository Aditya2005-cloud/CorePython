file=open("name.txt",'r')
content=file.read()
print(type(content))
print(content[0])
# students.txt
# John
# Alice
# Bob
# Python sees it like:
# "John\nAlice\nBob"