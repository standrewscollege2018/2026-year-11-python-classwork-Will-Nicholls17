'''Calculator made by Will'''

import random
import sys
import time

def calculator():
    print("Welcome to my calculator")
    #Name asker, error catching so the user doesn't input an empty name
    while True:
        name = input("Please enter your name > ")
        try:
            if name == "":
                print("Please enter a non empty name")
            else:
                print(f"\nWelcome to my calculator {name}")
                break
        except ValueError:
            print("Please enter a string")    
    def options():
        print("\nOptions")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide to divide two numbers")
        print("Enter 'random' to generate a random number")
        print("Enter 'quit' to end the program")
    
    options()

    while True:
        user_input = input("\nPlease enter your command > ")

        #Option to quit program
        if user_input == "quit":
            print(f"Thank you for using my program {name}")
            sys.exit()
        #Addition option, error catching for value and type error
        elif user_input == "add":
            print("-" * 30)
            print("Please enter the 2 numbers you wish to add\n")
            while True:
                try:
                    add_num1 = float(input("Please enter the first number > "))
                    if add_num1 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            while True:
                try:
                    add_num2 = float(input("Please enter your second number > "))
                    if add_num2 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            add_result = str(add_num1 + add_num2)
            time.sleep(1)
            print("-" * 30)
            print(f"\nThe answer is: {add_result}")
        #Subtraction option, error catching for value and type error
        elif user_input == "subtract":
            print("-" * 30)
            print("Please enter the 2 numbers you wish to subtract\n")
            while True:
                try:
                    subtract_num1 = float(input("Please enter the first number > "))
                    if subtract_num1 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            while True:
                try:
                    subtract_num2 = float(input("Please enter your second number > "))
                    if subtract_num2 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            subtract_result = str(subtract_num1 -subtract_num2)
            time.sleep(1)
            print("-" * 30)
            print(f"\nThe answer is: {subtract_result}")
        #Multiply option, error catching for value and type error
        elif user_input == "multiply":
            print("-" * 30)
            print("Please enter the 2 numbers you wish to multiply\n")
            while True:
                try:
                    multiply_num1 = float(input("Please enter the first number > "))
                    if multiply_num1 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            while True:
                try:
                    multiply_num2 = float(input("Please enter your second number > "))
                    if multiply_num2 == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    print("An error occured, please do it again")
            multiply_result = str(multiply_num1 * multiply_num2)
            time.sleep(1)
            print("-" * 30)
            print(f"\nThe answer is: {multiply_result}")
        #Division option, error catching for value, zero division and type error
        elif user_input == "divide":
            print("-" * 30)
            print("Please enter the 2 numbers you wish to divide\n")
            try:
                while True:
                    try:
                        divide_num1 = float(input("Please enter the first number > "))
                        if divide_num1 == "":
                            print("Please enter an actual number")
                        else:
                            break
                    except ValueError, TypeError:
                        print("An error occured, please do it again")
                while True:
                    try:
                        divide_num2 = float(input("Please enter your second number > "))
                        if divide_num2 == "":
                            print("Please enter an actual number")
                        else:
                            break
                    except ValueError, TypeError:
                        print("An error occured, please do it again")
                divide_result = str(divide_num1 / divide_num2)
                time.sleep(1)
                print("-" * 30)
                print(f"\nThe answer is: {divide_result}")
            except ZeroDivisionError:
                print("An error has occured due to zero division")
        #Random integer generator, uses while loops so that if there's a value error, it'll keep asking
        elif user_input == "random":
            print("-" * 30)
            print("What do you want the range to be?")
            while True:
                try:
                    random_integer_lower = int(input("Please enter the lowest number > "))
                    if random_integer_lower == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    ("Error occured, please do it again")
            while True:
                try:
                    random_integer_higher = int(input("Please enter the highest number > "))
                    if random_integer_higher == "":
                        print("Please enter an actual number")
                    else:
                        break
                except ValueError, TypeError:
                    ("Error occured, please do it again")
            random_integer = random.randint(random_integer_lower, random_integer_higher)
            time.sleep(1)
            print("-" * 30)
            print(f"\nThe random integer generated in: {random_integer}")   
calculator()