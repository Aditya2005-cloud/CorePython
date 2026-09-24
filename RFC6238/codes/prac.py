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
# So SHA-256 represented in hexadecimal always gives:
# 64 hexadecimal characters.
# Your result has 64 characters:c2aeccc42d2a579c281daae7e464a14d747924159e28617ad01850f0dd1bd135
print("-"*50)

text = b"hellow world"
result = hashlib.sha256(text)
print(result.hexdigest())

text = b"hello world"
result = hashlib.sha256(text)
print(result.hexdigest())


print("-"*50)


text1 = b"hellow world"
text2 = b"hello world"

hash1 = hashlib.sha256(text1)
hash2 = hashlib.sha256(text2)

print("Hash 1:")
print(hash1.hexdigest())

print("\nHash 2:")
print(hash2.hexdigest())

print("_"*50)

text = b"hello world"
hash1 = hashlib.sha256(text)
hash2 = hashlib.sha256(text)
print(hash1.hexdigest())
print(hash2.hexdigest())
print(hash1.hexdigest() == hash2.hexdigest())
# This demonstrates another important property: Same input → same hash

print("-"*50)

text = b"hello world"
result = hashlib.sha256(text)
print("Hex:")
print(result.hexdigest())
print("\nRaw bytes:")
print(result.digest())
print("\nType:")
print(type(result.digest()))
print("-"*50)
# HMAC : HMAC is not encryption HMAC creates a value that allows someone with the secret to verify the data.
        #      secret
        #         +
        #       message
        #         ↓
        #       HMAC
        #         ↓
        #  authentication code

import hmac
key= b"secret-key"
message=b"hello-world"
result = hmac.new(key,message,hashlib.sha256
)
print(result.hexdigest())
# key
#  │
#  │
#  ├──────────┐
#  │          │
#  ↓          ↓
# SECRET    MESSAGE
#  │          │
#  └────┬─────┘
#       ↓
#      HMAC
#       ↓
#  authentication code

print("-"*50)

key = b"my-secret"

message1 = b"hello world"
message2 = b"hello World"

hash1 = hmac.new(key, message1, hashlib.sha256)
hash2 = hmac.new(key, message2, hashlib.sha256)

print("Message 1:")
print(hash1.hexdigest())

print("\nMessage 2:")
print(hash2.hexdigest())