# dict 

school={"name": "ABC School", "location": "New York"}
school1={"name": "XYZ School", "location": "Los Angeles"}
add_school= school | school1
print(add_school)# Output: {'name': 'XYZ School', 'location': 'Los Angeles'} old value overwritten

school={"name": "ABC School", "location": "New York"}
school_info={"students": 500, "teachers": 30}
add_school= school | school_info
print(add_school) # Output: {'name': 'ABC School', 'location': 'New York', 'students': 500, 'teachers': 30} new key-value pairs added

student={"name": "John", "age": 20,
         "subjects":{"Math": 85, "Science": 90}}
print(student)
print(student["subjects"]["Math"]) # Output: 85
print(student.get("subjects"))
print(student.get("subjects").get("Science"))
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
student["gender"]={"Male","Female"}# Adding a new key-value pair we canuse list dict or set as value
print(student)
#add new subject
student["subjects"]["English"]=88
print(student)

student_copy=student.copy() # Shallow copy
print(student_copy)