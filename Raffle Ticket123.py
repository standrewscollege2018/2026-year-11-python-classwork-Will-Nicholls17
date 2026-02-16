'''Raffle Ticket Program'''

import random

import time

names = list()

print("Welcome to the raffle program")

keep_playing = True
while keep_playing:

    raffle_prize = input("What is the prize for the raffle? > ")

    raffle_cost_input = True
    while raffle_cost_input:
        try:
            raffle_cost = int(input(f"What is the cost of the {raffle_prize} (do not enter the $ sign)> "))
            if raffle_cost < 0:
                print("Invalid cost. Please enter a positive integer.")
            else:
                raffle_cost_input = False
        except ValueError: 
            print("Invalid. Please enter an integer")

    people_input = True
    while people_input:
        try:
            people = int(input("How many people are in the raffle? > "))
            if people < 0:
                print("Invalid number of people. Please enter a positive integer.")
            else:
                people_input = False
        except ValueError: 
            print("Invalid. Please enter an integer")



    for i in range(1, int(people) + 1):
        new_name = input("Enter name of person " + str(i) + ": ")
        names.append(new_name)

    winner = random.choice(names)
    input("Press Enter to continue...")
    print("-" * 30)
    print("Calculating the winner...")

    time.sleep(2)

    print(f"The winner of the {raffle_prize} that costs ${raffle_cost} is person number {names.index(winner) + 1} {winner}!")
    keep_playing_input = input("Do you want to play again? (yes/no) > ").lower()
    if keep_playing_input != "yes":
        keep_playing = False
        print("Thanks for playing the raffle program!")