''' This program demonstrates print(), data types, variables, inputs and f-strings'''

import random

print("Hi, Welcome to my program! I'm going to ask you some questions and then I'm going to give you some games to play. Let's get started!")

name = input("Firstly, what is your first name? >")

surname =  input(f"Secondly, what is your last name {name}? >")

print(f"Hello {name} {surname}")

LOWER_LIMIT = 1

UPPER_LIMIT = 100

answer = random.randint(LOWER_LIMIT, UPPER_LIMIT)

keep_asking = True

while keep_asking == True:
    
    guess_invalid = True

    while guess_invalid == True:
        try:
            guess = int(input(f'\nEnter a number between 1 and 100 {name} > ')) 

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
            answer = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        else: 
            keep_asking = False  
    elif guess > answer:
        print(f"Your guess is too high, {name} try again.")
    elif guess < answer:
        print(f"Your guess is too low, {name} try again.")
print(f"Thanks for playing {name} {surname}! Now we are going to play a different game. You are going to be a police officer and you have to catch a theif. In order to catch the theif, you must write a description of them. The thief is going to be hiding in one of the 3 rooms.You have to guess which room the thief is hiding in. Good luck {name} {surname}!")

correct_room = random.randint(1, 3)

keep_asking1 = True

theif_name = input(f"\nWhat is the name of the thief {name}? >")

theif_hair_color = input(f"What is the hair color of the thief {name}? >")

theif_weight_input = True
while theif_weight_input:
    try:
        theif_weight = int(input(f"What is the estimated weight of the thief {name}? >"))
        if theif_weight < 0:
            print("Invalid weight. Please enter a positive integer.")
        else:
            theif_weight_input = False
    except ValueError: 
        print("Invalid. Please enter an integer")

while keep_asking1 == True:
    
    guess_invalid1 = True

    while guess_invalid1 == True:
        try:
            guess1 = int(input(f"Now you are up to the rooms, please enter a number between 1 and 3 {name} > "))

            if guess1 >= 1 and guess1 <= 3:
                guess_invalid1 = False
            else:
                print("Error: Please enter a number between 1 and 3")
        except ValueError: 
            print("Invalid. Please enter an integer")
    
    if guess1 == correct_room:
        print(f"Congrats {name} {surname} you caught the thief!")
        keep_asking1 = False
        print(f"Congrats {name} {surname} you have completed the game! You have told the police the name of the thief, {theif_name}, the hair color of the thief {theif_hair_color}, and the estimated weight of the thief {theif_weight}kg!. You have also guessed which room the thief is hiding in. Thanks for playing!")
    else:
        print(f"Wrong room, {name} try again.")

print("Thanks for playing both my games, now I know that everyone needs a strong password, so I'm going to help you create one. I'm going to ask you some questions and then I'm going to generate a password for you. Let's get started!")

password_length_input = True
while password_length_input:
    try:
        password_length = int(input(f"What is the desired length of your password {name}? >"))
        if password_length < 0:
            print("Invalid length. Please enter a positive integer.")
        elif password_length > 100:
            print("Invalid length. Please enter a number less than or equal to 100.")
        else:
            password_length_input = False
    except ValueError: 
        print("Invalid. Please enter an integer")
        
include_letters = input(f"Do you want to include letters in your password {name}? (No caps) >")
include_numbers = input(f"Do you want to include numbers in your password {name}? (No caps) >")
include_special_characters = input(f"Do you want to include special characters in your password {name}? (No caps) >")
characters = ""
if include_numbers == "yes":
    include_numbers = True
    characters += "0123456789"
if include_special_characters == "yes":
    include_special_characters = True
    characters += "!@#$%^&*()-+"
if include_numbers == "no":
    include_numbers = False
if include_special_characters == "no":
    include_special_characters = False
if include_letters == "yes":
    include_letters = True
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"   
if include_letters == "no":
    include_letters = False
password = ""
for i in range(password_length):
    if include_letters == True:
        password += random.choice(letters)
    if include_numbers == True:
        password += random.choice("0123456789")
    if include_special_characters == True:
        password += random.choice("!@#$%^&*()-+")
print(f"Your generated password is: {password}. Thanks for playing {name} {surname}!")
