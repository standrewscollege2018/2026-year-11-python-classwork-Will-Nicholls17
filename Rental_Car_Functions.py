'''Rental car program with multiple lists and functions'''

import sys
#Lists for all the cars available to rent, the different names for the renters, whether or not the car is available to rent and the amount of seats in each car
cars = ["Suzuki Van (2)", "Toyota Corolla (4)", "Honda CRV (4)", "Suzuki Swift (4)", "Mitsubishi Airtrek (4)",
 "Nissan DC Ute (4)", "Toyota Previa (7)", "Toyota Hi Ace (12)", "Toyota Hi Ace (12)"]
names = ["", "", "", "", "", "", "", "", "", ""]
availability = [True, True, True, True, True, True, True, True, True]
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]

def view_names():
    for i in range(len(cars)):
        if availability[i] == False:
            print(f"{cars[i]} - {names[i]}")
    
def rental_car_program():
    run_program = True
    while run_program == True:
        print("Welcome to the University veichle rental system")
        print("The veichles are:")
        #For loop to see whether or not the car is available or not and if it isn't then it has an "unavailable status beside it"
        for i in range(len(cars)):
            if availability[i] == True:
                status = ""
            else:
                status = "- Unavailable"
            print(f"{i + 1}. {cars[i]} {status}")
        get_selection = True
        #A while loop to get the user input for the number car they want to rent
        while get_selection == True:
            try:
                rent_veichle_input = int(input("What car would you like to rent (press '0' to cancel program, '00' to view all the names of the people that rented the cars) and '000' to add a new car > "))
                #If statement to cancel program
                if rent_veichle_input == 00:
                    if names == "":
                        print("Please enter a name to see it")
                    else:
                        view_names()
                    
                elif rent_veichle_input == 000:
                    print("-" * 30)
                    new_car = input("Please enter the name of the new car")
                    try:
                        if new_car.strip == "":
                            print("Please enter a non - empty name")
                        else:
                            new_car.append(cars)
                    except ValueError, TypeError:
                        print("Please enter a valid input")

                    new_user_name = input("Please enter the name of the renter")
                    try:
                        if new_user_name.strip == "":
                            print("Please enter a non empty name")
                        else:
                            new_user_name.append(names)
                            True.append(availability)
                    except ValueError, TypeError:
                        print("Please a valid input")

                elif rent_veichle_input == 0:
                    sys.exit()
                #Elif statement to see whether or not the input for car to rent is within the right range
                elif rent_veichle_input < 0 or rent_veichle_input > len(cars):
                    print(f"Number must be between 1 and {len(cars)}")
                #Elif statement to see whether or not the car the user wants to rent has already been rented
                elif availability[rent_veichle_input-1] == False:
                    print("*** This vehicle is already booked. Please book another ***")
                else:
                    #While loop for the user entering name and if the user enters a blank name then it'll tell them to enter something
                    get_user_name = True
                    while get_user_name == True:
                        name = input("Enter your name: ")
                        if name.strip() == "":
                            print("You must enter something")
                        else:
                            # Put the renters name in the corresponding position in the renters list so it matches the car's position
                            names[rent_veichle_input-1] = name
                            get_user_name = False
                    #It will tell the user what car they booked
                    print(f"You have booked the {cars[rent_veichle_input-1]}")
                    availability[rent_veichle_input-1] = False
                    get_selection = False
                
            except ValueError, TypeError:
                print("Please enter a valid input")
        

rental_car_program()