'''A program that shows and displays a number of students and their driving license status'''
#Creates a list for the students, their current driving status and the valid driving status'.
students = ["Alan", "Brianna", "Charlie", "Dora"]
driving_status = ["No license", "No license", "Learners", "Restricted"]
valid_driving_status = ["Full", "No license", "Learners", "Restricted"]

#A function for constantly printing the student's names and their current driving status.
def display_students():
    print("\nStudent Driving Status List:")
    print("-" * 30)
    for i in range(len(students)):
        print(f"{i + 1}. {students[i]} - {driving_status[i]}")
    print("-" * 30)
    print("Enter 0 to quit and enter 10 to add a new user and their driving status.")
while True:
    #Prints the display students function in a while so it keeps going.
    display_students()
    try:
        choice = int(input("Select a student number to update: "))
        if choice == 0:
            print("Exiting program. Goodbye!")
            break
        elif choice >= len(students):
            print("Please enter a valid student number.")
        elif 1 <= choice <= len(students):
            new_status = input("Enter new status (No Licence, Learners, Restricted, Full): ").strip()
            if new_status in valid_driving_status:
                #This is what adds the new choice into the driving status.
                driving_status[choice - 1] = new_status
                print("\nStatus updated successfully!")
            else:
                #Error catching for incorrect words
                print("Invalid status entered. Please try again.")    
        if choice == 10:
            try:
                while True:
                    new_student_name = input("Enter the new person's name: ").capitalize().strip()
                    if new_student_name == "":
                        print("Please a non - empty name")
                    elif new_student_name in students:
                        print("Please enter a new driver name.")                    
                    else:
                        students.append(new_student_name)
                        break
                while True:
                    new_student_status = input("Enter the new person's driving status: ").strip()
                    if new_student_status in valid_driving_status:
                        driving_status.append(new_student_status)
                        break
                    else:
                        ("Please enter a valid driving status.")
            except ValueError:
                 print("Invalid input. Please enter a valid input.")
    except ValueError:
        #Error catching for incorrect value
        print("Invalid input. Please enter a number.")    