import _sqlite3
from secrets import choice
DATABASE = 'students.db'
#Connect to the database and create a cursor
connection = _sqlite3.connect(DATABASE)
cursor = connection.cursor()


def view_student_information():
    #Function to view more information about a student, with error handling for invalid choices and no students
    print("\nTo view all information about a student, enter their number. To return to the menu, enter 0.")
    choice = input("Enter your choice: ")
    if choice == "0":
        return
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input.")
        return
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    if 1 <= choice <= len(results):
        student = results[choice - 1]
        print(f"\nName: {student[1]} {student[2]}")
        print(f"Tutor Group: {student[3]}")
        print(f"City: {student[4]}")
    else:
        print("Invalid number.")

def no_students():
    #Error catching function to check if there are no students in the database
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    if not results:
        print("No students found.")
        return True
    return False

#Display function to show results in a formatted way
def display_students(results):
    print(f"\n{'No.':<5}{'Name':20}{'Tutor Group':15}{'City'}")
    print("-" * 50)

    for i, student in enumerate(results, start=1):
        name = f"{student[1]} {student[2]}"
        print(f"{i:<5}{name:20}{student[3]:15}{student[4]}")
    print("-" * 50)
    print(f"{len(results)} result(s)")
    view_student_information()

def search_students_name(): 
    #Function to search students by name, with error handling for no students and empty search terms
    if no_students() == True:
        return
    keep_asking_student_name = True
    while keep_asking_student_name == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter search term for student name (0 to cancel): ")
        if search == "":
            print("Search term cannot be empty. Please try again.")
        if search == "0":
            if cancel_operation():
                return
        else:
            keep_asking_student_name = False
            search = f"%{search}%"
    #Execute the SQL query to search for students by name, using the LIKE operator for partial matching
    cursor.execute("SELECT * FROM student WHERE first_name LIKE ? OR LAST_NAME LIKE ?", (f"%{search}%", f"%{search}%"))
    results = cursor.fetchall()
    display_students(results)
    print("-" * 30)

def search_students_tutor_group():
    if no_students() == True:
        return
    #Function to search students by tutor group
    keep_asking_tutor_group = True
    while keep_asking_tutor_group == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter tutor group (0 to cancel): ")
        if search == "0":
            if cancel_operation():
                return
        if search == "":
            print("Search term cannot be empty. Please try again.")
        if len(search) > 3:
            print("Tutor group must be 3 characters or less. Please try again.")
        else:
            keep_asking_tutor_group = False
            search = f"%{search}%"
    #Execute the SQL query to search for students by tutor group, using the LIKE operator for partial matching
    cursor.execute("SELECT * FROM student WHERE tutor_group LIKE ?", (f"%{search}%",)) 
    tutor_results = cursor.fetchall()
    display_students(tutor_results)
    print("-" * 30)

def search_students_city():
    if no_students() == True:
        return
    #Function to search students by city
    keep_asking_city = True
    while keep_asking_city == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter city (0 to cancel): ")
        if search == "0":
            if cancel_operation():
                return
        if search == "":
            print("Search term cannot be empty. Please try again.")
        else:
            keep_asking_city = False
            search = f"%{search}%"
    #Execute the SQL query to search for students by city, using the LIKE operator for partial matching, don't forget comma
    cursor.execute("SELECT * FROM student WHERE city LIKE ?", (f"%{search}%",))
    city_results = cursor.fetchall()
    display_students(city_results)
    print("-" * 30)

def error_catch_empty_input(prompt):
    keep_asking_error_catch_empty_input = True
    while keep_asking_error_catch_empty_input == True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please try again.")
        else:
            keep_asking_error_catch_empty_input = False
            return value

def cancel_operation():
    print("-" * 30)
    choice = input("Do you want to cancel this operation? (y/n):")
    print("-" * 30)
    if choice.lower() == "y":
        print("Operation cancelled.")
        return True
    else:
        return False

#Add a student to the database, with error handling for empty inputs
def add_student():
    keep_asking_add_student_first = True
    while keep_asking_add_student_first == True: 
        first = error_catch_empty_input("First name (0 to cancel): ")
        if first == "0":
            if cancel_operation():
                return
        else:     
            print("-" * 30)       
            keep_asking_add_student_first = False

    keep_asking_add_student_last = True
    while keep_asking_add_student_last == True:
        last = error_catch_empty_input("Last name (0 to cancel): ")
        if last == "0":
            if cancel_operation():
                return
        else: 
            print("-" * 30)           
            keep_asking_add_student_last = False       

    keep_asking_add_student_tutor = True
    while keep_asking_add_student_tutor == True:
        tutor = error_catch_empty_input("Tutor group (0 to cancel): ")
        if tutor == "0":
            if cancel_operation():
                return
        else:
            print("-" * 30)
            keep_asking_add_student_tutor = False

    keep_asking_add_student_city = True
    while keep_asking_add_student_city == True:
        city = error_catch_empty_input("City (0 to cancel): ")
        if city == "0":
            if cancel_operation():
                return
        else:        
            print("-" * 30)    
            keep_asking_add_student_city = False

    if not (first and last and tutor and city):
        print("All fields required.")
        return

    cursor.execute(
        "INSERT INTO student (first_name, last_name, tutor_group, city) VALUES (?, ?, ?, ?)",
        (first, last, tutor, city)
    )
    connection.commit()
    print("Student added!")


#Delete student from the database, with error handling for no students and invalid choices
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

def delete_all_students():
    #Function to delete all students from the database, with error handling for no students and confirmation before deleting
    cursor.execute("SELECT * FROM student")
    confirm = input("Are you sure you want to delete all students? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM student")
        connection.commit()
        print("\nAll students deleted!")
    else:
        print("Operation cancelled.\n")

def main():
    keep_asking = True
    while keep_asking == True:
        #Print the menu for the user to choose how they want to search the database, and call the corresponding function based on their choice
        print("\nWelcome to the student database!")
        print("=" * 30)
        print("Menu:")
        print("-" * 30)
        print("1. Search by name")
        print("2. Search by tutor group")
        print("3. Search by city")
        print("4. Add student")
        print("5. Delete student")
        print("6. View all students")
        print("7. Delete all students")
        print("8. Exit")
        print("-" * 30)
        #Choice input to go to functions based on user input, and error catching for invalid choices, also option to exit the program
        choice = input("Enter your choice: ")
        if choice == "1":
            print("-" * 30)
            search_students_name()
        elif choice == "2":
            print("-" * 30)
            search_students_tutor_group()       
        elif choice == "3":
            print("-" * 30)
            search_students_city()
        elif choice == "4":
            print("-" * 30)
            add_student()
        elif choice == "5":
            print("-" * 30)
            delete_student()
        elif choice == "6":
            print("-" * 30)
            cursor.execute("SELECT * FROM student")
            results = cursor.fetchall()
            display_students(results)
        elif choice == "7":
            print("-" * 30)
            delete_all_students()
        elif choice == "8":
            keep_asking = False
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()