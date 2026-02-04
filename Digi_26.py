''' This program demonstrates print(), data types, variables, inputs and f-strings'''

# print() is a function that outputs whatever is inside the brackets
#numbets can be included directly in the brackets
print(123)

#when printing text, it must be in speechmarkers which turns it into a string
print("Hello")

name = input("what is your name?")

surname =  input("What is your surname?")

print(f"Hello {name} {surname}")

print(f"{'left aligned text' : <20}")

number = input("choose a number 0 - 100")

if number >=100 