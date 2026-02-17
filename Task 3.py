'''Number between 50 and 100'''
total = 0
while total <= 200:
    try:
        num = float(input("Enter a number between 50 and 100: > "))
        if 50 <= num <= 100:
            total += num
        else:
            print("The number is not between 50 and 100. Please enter it again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"The grand total is {total}.")