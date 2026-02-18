'''The Fibonacci series calculator'''
keep_asking = True
while keep_asking:
    try:
        num_terms = int(input("How many terms of the Fibonacci series do you want to see? > "))
        if num_terms > 0:
            keep_asking = False
        elif num_terms == 0:
            print("The Fibonacci series has no terms. Please enter a positive integer.")
        elif num_terms > 650:
            print("That's a lot of terms! Please enter a smaller positive integer.")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
a, b = 1, 1
for i in range(num_terms):
    print(a)
    a, b = b, a + b