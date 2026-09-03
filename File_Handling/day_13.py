file=open("students.txt","r")# uou can also use file path like "D:\\File_Handling\\students.txt"
content=file.read()
file.close()#we close the file after reading
print(content)