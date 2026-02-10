'''Grade checker'''

Grade_A = 90
Grade_B = 70
Grade_C = 50
Grade_Fail = 0
Try_Again = True
while Try_Again == True:
    try:
        grade = int(input("Enter your grade: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if grade >= Grade_A:
        print("You got an A!")
    elif grade >= Grade_B:
        print("You got a B!")
    elif grade >= Grade_C:
        print("You got a C!")
    elif grade >= Grade_Fail:
        print("You failed.")
    else:
        print("Invalid grade.")
    Try_AgainI = input("Do you want to try again? (yes/no): ")
    if Try_AgainI.lower() == "yes":
        Try_Again = True
    elif Try_AgainI.lower() == "no":
        print("Goodbye!")
        Try_Again = False
    else:
        print("Invalid input. Exiting the program.")
        Try_Again = False
    
