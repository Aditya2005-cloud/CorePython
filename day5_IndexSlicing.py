name="Kaka"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#or
print("____________________________________")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
#or
print("____________________________________")
for i in range(len(name)):
    print(name[i])
#or
print(name[0:4])# start from 0 and end at 3(4-1)
print(name[::])
print(name[::-1])#reverse
print(name[::2])#skip by 2 in kaka it will print k then skpi a and the again print k again skip a same fro minus but in reverse
#MINI PROJECT (Program should print:Total characters,Total vowels,Reversed string)
userName=input("Enter your name: ")
userName=userName.lower()
counting=0
print("Total characters: ",len(userName))
# for i in range(len(userName)):
#     if userName[i] in "aeiou":#better way
#     # if userName[i]=="a" or userName[i]=="e" or userName[i]=="i" or userName[i]=="o" or userName[i]=="u":
#         print(userName[i])
#         counting+=1
for ch in userName:#better way
    if ch in "aeiou":
        counting += 1
print("Total vowels: ",counting)
print("Reversed string: ",userName[::-1])