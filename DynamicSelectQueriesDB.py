import _sqlite3
from secrets import choice
DATABASE = 'students.db'
#Connect to the database and create a cursor
connection = _sqlite3.connect(DATABASE)
cursor = connection.cursor()

def search_students_name():
    #Function to search students by name
    keep_asking_student_name = True
    while keep_asking_student_name == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter search term for student name: ")
        if search == "":
            print("Search term cannot be empty. Please try again.")
        else:
            keep_asking_student_name = False
            search = f"%{search}%"
    #Execute the SQL query to search for students by name, using the LIKE operator for partial matching
    cursor.execute("SELECT * FROM student WHERE first_name LIKE ? OR LAST_NAME LIKE ?", (f"%{search}%", f"%{search}%"))

    results = cursor.fetchall()
    num_results = len(results)
    print(f"\nStudents with names containing '{search.strip('%')}':")
    #Print the results in a formatted way, showing the name and tutor group of each student
    print(f"{'Name':20} {'Tutor group'}")
    print("-" * 30)
    for student in results:
        name = f"{student[1]} {student[2]}"

        print(f"{name:20} {student[3]}")
    print("-" * 30)
    #Print the number of results found
    print(f"\n{num_results} result(s) found.")
    print("-" * 30)

def search_students_tutor_group():
    #Function to search students by tutor group
    keep_asking_tutor_group = True
    while keep_asking_tutor_group == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter tutor group: ")
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
    num_results = len(tutor_results)
    print(f"\nStudents in tutor group containing '{search.strip('%')}':")
    print(f"{'Name':20} {'Tutor group'}")
    print("-" * 30)
    for student in tutor_results:
        #Print the name and tutor group of each student in a formatted way
        name = f"{student[1]} {student[2]}"

        print(f"{name:20} {student[3]}")
    print("-" * 30)
    #Print the number of results found
    print(f"\n{num_results} result(s) found.")
    print("-" * 30)

def search_students_city():
    #Function to search students by city
    keep_asking_city = True
    while keep_asking_city == True:
        #Error catching as to not allow the user to enter an empty search term
        search = input("Enter city: ")
        if search == "":
            print("Search term cannot be empty. Please try again.")
        else:
            keep_asking_city = False
            search = f"%{search}%"
    #Execute the SQL query to search for students by city, using the LIKE operator for partial matching, don't forget comma
    cursor.execute("SELECT * FROM student WHERE city LIKE ?", (f"%{search}%",))

    city_results = cursor.fetchall()
    num_results = len(city_results)
    print(f"\nStudents from city containing '{search.strip('%')}':")
    #Print the name and city of each student in a formatted way
    print(f"{'Name':20} {'City'}")
    print("-" * 30)
    for student in city_results:
        name = f"{student[1]} {student[2]}"

        print(f"{name:20} {student[4]}")
    print("-" * 30)
    #Print the number of results found
    print(f"\n{num_results} result(s) found.")
    print("-" * 30)


keep_asking = True
while keep_asking == True:
    #Print the menu for the user to choose how they want to search the database, and call the corresponding function based on their choice
    print("Welcome to the student database!")
    print("=" * 30)
    print("Menu:")
    print("-" * 30)
    print("1. Search by name")
    print("2. Search by tutor group")
    print("3. Search by city")
    print("4. Exit")
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
        keep_asking = False
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")