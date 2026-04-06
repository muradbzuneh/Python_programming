import json

students = []
FILE_NAME = "students_data.json"

# ================= FILE HANDLING =================

def load_data():
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except:
        students = []

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)

# ================= VALIDATION =================

def input_non_empty(text):
    while True:
        value = input(text).strip()
        if value == "":
            print("This field cannot be empty!")
        else:
            return value

# STUDENT ID VALIDATION
def input_student_id():
    while True:
        sid = input("Enter Student ID (WOUR/XXXX/XX): ")

        parts = sid.split("/")

        if len(parts) != 3 or parts[0] != "WOUR":
            print("Invalid format! Use WOUR/XXXX/XX")
            continue

        if not (parts[1].isdigit() and parts[2].isdigit()):
            print("ID must contain numbers only!")
            continue

        return sid

# DEPARTMENT SELECTION
def choose_department():
    departments = [
        "Software Engineering",
        "Computer Science",
        "Information System",
        "Information Technology"
    ]

    print("\nChoose Department:")
    for i, d in enumerate(departments, 1):
        print(f"{i}. {d}")

    while True:
        choice = input("Enter choice (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            return departments[int(choice) - 1]
        else:
            print("Invalid choice! Select 1-4")

# ================= MENU =================

def show_menu():
    print("\n" + "="*50)
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student (ID or Name)")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View by Department")
    print("7. Sort Students")
    print("8. GPA Statistics")
    print("9. Exit")
    print("="*50)

# ================= FEATURES =================

def add_student():
    print("\n--- ADD STUDENT ---")

    student_id = input_student_id()

    for s in students:
        if s["id"] == student_id:
            print("ID already exists!")
            return

    name = input_non_empty("Enter Name: ")
    dept = choose_department()

    while True:
        try:
            gpa = float(input("Enter GPA (0–4): "))
            if 0 <= gpa <= 4:
                break
            else:
                print("GPA must be 0–4")
        except:
            print("Invalid GPA!")

    students.append({
        "id": student_id,
        "name": name,
        "department": dept,
        "gpa": gpa
    })

    save_data()
    print("Student added!")

# ------------------------

def view_all_students():
    if not students:
        print("No students found!")
        return

    print("\nNo  ID             Name        Dept                     GPA")
    print("-"*70)

    for i, s in enumerate(students, start=1):
        print(f"{i:<3} {s['id']:<14} {s['name']:<10} {s['department']:<25} {s['gpa']:.2f}")

# ------------------------

def search_student():
    keyword = input("Enter ID or Name: ").lower()

    found = False

    for s in students:
        if keyword in s["id"].lower() or keyword in s["name"].lower():
            print(s)
            found = True

    if not found:
        print("No matching student found!")

# ------------------------

def update_student():
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            print("Leave blank to keep old value")

            new_name = input("New Name: ")
            if new_name:
                s["name"] = new_name

            print("Change department? (y/n)")
            if input().lower() == "y":
                s["department"] = choose_department()

            new_gpa = input("New GPA: ")
            if new_gpa:
                s["gpa"] = float(new_gpa)

            save_data()
            print("Updated!")
            return

    print("Student not found!")

# ------------------------

def delete_student():
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data()
            print("Deleted!")
            return

    print("Student not found!")

# ------------------------

def view_by_department():
    dept = choose_department()

    found = False
    for s in students:
        if s["department"] == dept:
            print(s)
            found = True

    if not found:
        print("No students in this department!")

# ------------------------

def sort_students():
    print("\n1. Name A-Z")
    print("2. Name Z-A")
    print("3. GPA High-Low")
    print("4. GPA Low-High")

    choice = input("Choose: ")

    if choice == "1":
        students.sort(key=lambda x: x["name"])
    elif choice == "2":
        students.sort(key=lambda x: x["name"], reverse=True)
    elif choice == "3":
        students.sort(key=lambda x: x["gpa"], reverse=True)
    elif choice == "4":
        students.sort(key=lambda x: x["gpa"])
    else:
        print("Invalid choice!")
        return

    print("Sorted!")

# ------------------------

def gpa_statistics():
    if not students:
        print("No students!")
        return

    gpas = [s["gpa"] for s in students]

    avg = sum(gpas) / len(gpas)
    highest = max(gpas)
    lowest = min(gpas)

    print("\n--- GPA REPORT ---")
    print("Average GPA:", round(avg, 2))
    print("Highest GPA:", highest)
    print("Lowest GPA:", lowest)

    print("\nTop Students:")
    for s in students:
        if s["gpa"] == highest:
            print(s)

    print("\nLowest Students:")
    for s in students:
        if s["gpa"] == lowest:
            print(s)

    excellent = good = average = poor = 0

    for g in gpas:
        if g >= 3.5:
            excellent += 1
        elif g >= 3.0:
            good += 1
        elif g >= 2.0:
            average += 1
        else:
            poor += 1

    print("\n--- Grade Distribution ---")
    print("Excellent:", excellent)
    print("Good:", good)
    print("Average:", average)
    print("Poor:", poor)

# ================= MAIN =================

load_data()

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        view_by_department()
    elif choice == "7":
        sort_students()
    elif choice == "8":
        gpa_statistics()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

    input("\nPress Enter to continue...")