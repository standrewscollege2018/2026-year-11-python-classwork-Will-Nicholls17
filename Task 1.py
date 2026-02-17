'''Which number is bigger?'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"You entered {num1} and {num2}.")
if num1 > num2:
    print(f"The larger number is {num1}.")
elif num2 > num1:
    print(f"The larger number is {num2}.")
else:
    print("The two numbers are equal.")
total = num1 + num2
print(f"The total of the two numbers is {total}.")