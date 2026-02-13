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

