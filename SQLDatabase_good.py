import sqlite3

DATABASE = 'students.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


#Display function to show results in a formatted way
def display_students(results):
    print(f"\n{'No.':<5}{'Name':20}{'Tutor Group':15}{'City'}")
    print("-" * 50)

    for i, student in enumerate(results, start=1):
        name = f"{student[1]} {student[2]}"
        print(f"{i:<5}{name:20}{student[3]:15}{student[4]}")

    print("-" * 50)
    print(f"{len(results)} result(s)\n")


#Search functions to query the database based on user input, with error handling for empty inputs and invalid tutor groups
def search_students_name():
    search = input("Enter name: ").strip()
    if not search:
        print("Search cannot be empty.")
        return

    cursor.execute(
        "SELECT * FROM student WHERE first_name LIKE ? OR last_name LIKE ?",
        (f"%{search}%", f"%{search}%")
    )

    results = cursor.fetchall()
    display_students(results)


def search_students_tutor_group():
    search = input("Enter tutor group: ").strip()

    if not search or len(search) > 3:
        print("Invalid tutor group.")
        return

    cursor.execute(
        "SELECT * FROM student WHERE tutor_group LIKE ?",
        (f"%{search}%",)
    )

    results = cursor.fetchall()
    display_students(results)


def search_students_city():
    search = input("Enter city: ").strip()
    if not search:
        print("Search cannot be empty.")
        return

    cursor.execute(
        "SELECT * FROM student WHERE city LIKE ?",
        (f"%{search}%",)
    )

    results = cursor.fetchall()
    display_students(results)


# ---------- ADD STUDENT ----------
def add_student():
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    tutor = input("Tutor group: ").strip()
    city = input("City: ").strip()

    if not (first and last and tutor and city):
        print("All fields required.")
        return

    cursor.execute(
        "INSERT INTO student (first_name, last_name, tutor_group, city) VALUES (?, ?, ?, ?)",
        (first, last, tutor, city)
    )
    connection.commit()
    print("Student added!\n")


# ---------- DELETE STUDENT ----------
def delete_student():
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()

    if not results:
        print("No students to delete.")
        return

    display_students(results)

    try:
        choice = int(input("Enter number to delete (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 0:
        return

    if 1 <= choice <= len(results):
        student_id = results[choice - 1][0]

        cursor.execute("DELETE FROM student WHERE id = ?", (student_id,))
        connection.commit()

        print("Student deleted!\n")
    else:
        print("Invalid number.")


# ---------- MAIN MENU ----------
def main():
    while True:
        print("Student Database")
        print("=" * 30)
        print("1. Search by name")
        print("2. Search by tutor group")
        print("3. Search by city")
        print("4. Add student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choice: ")

        if choice == "1":
            search_students_name()
        elif choice == "2":
            search_students_tutor_group()
        elif choice == "3":
            search_students_city()
        elif choice == "4":
            add_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


# ---------- RUN ----------
if __name__ == "__main__":
    main()