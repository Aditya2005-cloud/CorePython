# First advanced concept: bytes vs str

name = "Aditya"# its a string
data=b"hello"#its bytes

print(name)
print(data)

print(type(name))
print(type(data))

print(data.hex())
# print(name.hex()) cannot convert string to bytes

# _________________________________________________________________________________________________
print("_"*50)
# Why do we need bytes?

# Because cryptographic algorithms don't work with Python's concept of "text."

import hashlib

# text="hellow world"
# hashlib.sha256(text) you will get error as txt is not a bytes object its a string

text=b"hellow world"
# or we can convert str to bytes
text1="hellow"
data=text1.encode()
print(data)
print(type(data))

result=hashlib.sha256(text)#it doesn't directly give you the final hash as a normal string.It gives you a HASH object.

print("Hash object:")
print(result)
print(result.hexdigest)# prove of HASH object.
print(type(result))

print("\nHex digest:")
print(result.hexdigest())

