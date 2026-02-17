'''Which number is bigger, enter a name bigger than the first.'''
num1 = float(input("Enter the first number: "))
keep_asking = True
while keep_asking:
    try:
        num2 = float(input("Enter a second number that is greater than the first: "))
        if num2 > num1:
            print(f"The two numbers you entered are {num1} and {num2}.")
            keep_asking = False
        else:
            print("The second number is not greater than the first. Enter it again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")