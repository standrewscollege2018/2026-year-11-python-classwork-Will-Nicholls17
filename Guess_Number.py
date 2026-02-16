'''A game where you guess a number 1 - 10'''

import random

#Finds a random number between 1 and 10 and stores it in a variable called NUMBER
NUMBER = random.randint(1, 10)
keep_asking = True
while keep_asking == True:
    guess = int(input("Guess a number between 1 and 10 : "))
    if guess == NUMBER:
        print("That's right!")
        play_again = input("Do you want to play again? (No caps) >")
        if play_again == "yes":
            NUMBER = random.randint(1, 10)
            keep_asking = True
        else: 
            keep_asking = False  
    elif guess > NUMBER:
        print("Nope that's wrong try again.")
    elif guess < NUMBER:
        print("Your guess is too low, try again.")