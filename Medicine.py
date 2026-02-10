'''A program to check how much medicine you need to take based on your age and weight.'''

AGE_LIMIT = int(input("Please enter your age: "))
WEIGHT_LIMIT = int(input("Please enter your weight in KG: "))
print("Welcome to the medicine checker! Please enter your age and weight to find out how much medicine you need to take.")
if AGE_LIMIT < 9:
    print("You are too young to take this medicine.")
elif AGE_LIMIT >= 9 and AGE_LIMIT <= 12:
    if WEIGHT_LIMIT < 30:
        print("You need to take 1 tablet.")
    else:
        print("You need to take 2 tablets.")
else:
    if WEIGHT_LIMIT < 50:
        print("You need to take 2 tablets.")
    else:
        print("You need to take 3 tablets.")