students=[]
def add_student():
    student={"name":input("Enter student name: "),
             "marks":int(input("Enter student marks: "))}
    students.append(student)
def show_students():   
    for student in students:
        print(f"Name: {student['name']}")
def topper():
    top=0
    for student in students:
        if student["marks"]>top:
            top=student["marks"]
    for student in students:
        if student["marks"]==top:
            print(f"Name: {student['name']}")

def main():
    while True:
        print("1. Add Student")
        print("2. Show Students")
        print("3. Topper")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            topper()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()