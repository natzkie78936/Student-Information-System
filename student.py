import json

students = {}
filename = "students.json"

def load_data():
    global students
    try:
        with open(filename, "r") as f:
            students = json.load(f)
        print("Data loaded successfully!\n")
    except FileNotFoundError:
        students = {}
        print("No saved data found.\n")

def save_data():
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)
    print("Data saved successfully!\n")

calc_average = lambda grades: sum(grades) / len(grades) if grades else 0

def add_student():
    sid = input("Enter student ID: ")
    if sid in students:
        print("Student already exists!\n")
        return
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grades = input("Enter grades separated by spaces: ").split()
    grades = [int(g) for g in grades] if grades else []
    students[sid] = {"name": name, "age": int(age), "grades": grades}
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")
        print("Grades:", info["grades"])
        if info["grades"]:
            avg = calc_average(info["grades"])
            print(f"Average: {avg:.2f}\n")
        else:
            print("No grades available.\n")

def update_student():
    sid = input("Enter student ID to update: ")
    if sid not in students:
        print("Student not found!\n")
        return
    name = input("Enter new name (leave blank to keep current): ")
    age = input("Enter new age (leave blank to keep current): ")
    grades = input("Enter new grades separated by spaces (leave blank to keep current): ")
    if name:
        students[sid]["name"] = name
    if age:
        students[sid]["age"] = int(age)
    if grades:
        students[sid]["grades"] = [int(g) for g in grades.split()]
    print("Student updated successfully!\n")

def delete_student():
    sid = input("Enter student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")




while True:
        print("""
----- Student Information System -----
1. Add Student
2. Display Students
3. Update Student
4. Delete Student
5. Save to File
6. Load from File
7. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


