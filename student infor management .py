# Initialize empty lists and dictionary
students_list = []
students_dict = {}

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    # Add student information to lists and dictionary
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    
    print("Student information added successfully.")

def view_students():
    print("Student Details:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

def search_student():
    name = input("Enter student name to search: ")
    if name in students_dict:
        info = students_dict[name]
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

# Main program loop
while True:
    print("\nStudent Information Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        remove_student()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
