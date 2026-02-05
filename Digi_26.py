''' This program demonstrates print(), data types, variables, inputs and f-strings'''

import random

name = input("Hello, what is your first name? >")

surname =  input(f"What is your last name {name}? >")

print(f"Hello {name} {surname}")

LOWER_LIMIT = 1

UPPER_LIMIT = 100

answer = random.randint(1, 100)

keep_asking = True

while keep_asking == True:
    
    guess_invalid = True

    while guess_invalid == True:
        try:
            guess = int(input(f'\nEnter a number {name} > ')) 

            if guess >= LOWER_LIMIT and guess <= UPPER_LIMIT:
                guess_invalid = False
            else:
                print(f"Error: Please enter a number between {LOWER_LIMIT} and {UPPER_LIMIT}")
        except ValueError: 
            print("Invalid. Please enter an integer")
    
    if guess == answer:
        print(f"Congrats {name} {surname} your guess is correct!")
        play_again = input("Do you want to play again? (No caps) >")
        if play_again == "yes":
            keep_asking = True
            answer = random.randint(1, 100)
        else: 
            keep_asking = False  
    elif guess > answer:
        print(f"Your guess is too high, {name} try again.")
    elif guess < answer:
        print(f"Your guess is too low, {name} try again.")