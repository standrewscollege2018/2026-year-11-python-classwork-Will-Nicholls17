''' Rental car program with multiple lists '''

# Set up lists for car names, seats and availability
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
availability = [True, True, True, True, True, True, True, True, True]
renters = ["", "", "", "", "", "", "", "", ""]

# Run the program in a loop so user can keep making changes
run_program = True
while run_program == True:
    # Display title and list of vehicles
    print("Welcome to the University vehicle rental system")
    print("The vehicles are:")
    # Display cars in a numbered list
    for i in range(len(cars)):
        # Check if current car is available
        # Variable called status is blank if available
        if availability[i -1] == True:
            status = ""
        else:
            status = "- (Unavailable)"

        print(f"{i+1}. {cars[i]} ({seats[i]}) {status}")

    # Ask user what vehicle they want to book
    # Error catching stops them entering invalid inputs like a string or a number outside the range of the number of cars
    get_selection = True
    while get_selection == True:
        try:
            selection = int(input("What vehicle would you like to book? "))
            # If user enters 0 as their selection then the program stops asking them for a vehicle to book
            if selection == 0:
                get_selection = False
                run_program = False
            # Check if selection is in range
            elif selection < 0 or selection > len(cars):
                print(f"Number must be between 1 and {len(cars)}")
            # Check if selected car is available
            elif availability[selection-1] == False:
                print("*** This vehicle is already booked. Please book another ***")
            else:
                # Get their name for the booking
                # Error catch to prevent blank names
                get_name = True
                while get_name == True:
                    name = input("Enter your name: ")
                    if name.strip() == "":
                        print("You must enter something")
                    else:
                        # Put their name in the corresponding position in the renters list so it matches the car's position
                        renters[selection-1] = name
                        get_name = False
                print(f"You have booked the {cars[selection-1]}")
                availability[selection-1] = False
                get_selection = False
        except ValueError, TypeError:
            ("Invalid, do it again")
    # Program ends by printing a summary of the rentals today
    for i in range(len(cars)):
        if availability[i] == False:
            print(f"{cars[i]} - {renters[i]}")