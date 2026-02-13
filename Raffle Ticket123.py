'''Raffle Ticket Program'''

import random

names = list()

print("Welcome to the raffle program")

raffle_prize = input("What is the prize for the raffle? > ")

raffle_cost = int(input(f"What is the cost of the {raffle_prize} (do not enter the $ sign)> "))

people = input("How many people are in the raffle? > ")

for i in range(1, int(people) + 1):
    new_name = input("Enter name of person " + str(i) + ": ")
    names.append(new_name)

winner = random.choice(names)

print(f"The winner of the {raffle_prize} that costs ${raffle_cost} is person number {names.index(winner) + 1} {winner}!")