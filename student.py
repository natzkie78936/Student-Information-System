import json

students = {}

def load():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                sid, name, age, *grades = line.strip().split(",")
                grades = [int(g) for g in grades[0].split()] if grades else []
                students[sid] = {"name": name, "age": int(age), "grades": grades}
        print("Records loaded from students.txt!\n")
    except FileNotFoundError:
        print("No file found. Starting with empty records.\n")

def save():
    with open("students.txt", "w") as f:
        for sid, info in students.items():
            grades_str = " ".join(map(str, info["grades"]))
            f.write(f"{sid},{info['name']},{info['age']},{grades_str}\n")
    print("Records saved to students.txt!\n")

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
            save()
        elif choice == "6":
            load()
        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


