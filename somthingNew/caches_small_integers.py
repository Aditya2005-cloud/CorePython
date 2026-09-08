# a = 256
# b = 256
# print(a is b)   # True  ← same object in memory!
# In a SCRIPT FILE — Python compiler sees both lines at once
# Compiler thinks: "these are the same constant in the same block"
# → optimizes them to point to the SAME object → True
a = 257
b = 257
print(a is b)   
# In REPL — each line compiled separately
a = int("257")
b = int("257")

print(a == b)   # True
print(a is b)   # False ← NOW see the expected behavior


print("-"*50)


a = [10, 20]
b = a
a.append(30)
print(a)
print(b)# [10, 20, 30] how does this happen?

# proving the same object

a = [10, 20]
b = a
print(a is b)   # True
b.append(30)
print(a)        # [10, 20, 30]
print(b)        # [10, 20, 30]

print("-"*50)

a = [1, 2, 3]
b = a
b = b + [4]
print(a)
print(b)
print(a is b)#This is the trick. + creates a new list object.So it will be False

print("-"*50)

a = [1, 2, 3]
b = a
b.append(4)
print(a is b)

print("-"*50)

a = [1, 2]
b = a
a += [3]
print(a)
print(b)
print(a is b)

print("-"*50)

a = [1, 2]
print(a)
print(a.__iadd__([3]))#The list can modify itself.
print(a)

print("-"*50)

a = "hello"
b = a
a += " world"
print(a)
print(b)
print(a is b)

print("-"*50)

a = [1, 2]
b = a

a = a + [3]#its creat a new object in memory

b += [4]

print(a)
print(b)
print(a is b)

print("-"*50)

def add_item(item, box=[]):
    box.append(item)
    return box

print(add_item("A"))
print(add_item("B"))
print(add_item("C"))