'''Demonstrates the use of a for loop.'''

import random

for i in range(18, 23):
    print(i)


number = int(input("How many names would you like to enter? "))

for i in range(0, number):
    name = input("Enter a name: ")
    print(f"Hello {name}")


'''Fizz Buzz game'''

number1 = int(input("How many numbers would you like to enter for fizz buzz game? "))

for i in range(1, number1 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("All done!")

print("Welcome to the raffle program")

raffle_prize = input("What is the prize for the raffle? > ")

raffle_cost = int(input(f" What is the cost of the {raffle_prize} (do not enter the $ sign)> "))

people = input("How many people are in the raffle? > ")

for i in range(1, int(people) + 1):
    name = input("Enter name of person " + str(i) + ": ")

winner = random.choice(name)

print(f"The winner of the {raffle_prize} that costs ${raffle_cost} is person number {winner}!")