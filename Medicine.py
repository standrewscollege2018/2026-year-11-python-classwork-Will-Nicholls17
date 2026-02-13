'''A program to check how much medicine you need to take based on your age and weight.'''

print("Welcome to the digital pharmacy, we're going to give you a recomended amount of paracetamol to take based on your age and weight. The recommend 4- 6 hourly dose of parcetomol for children under 12 years is 10 milligrams of paracetomol per kilogram of body weight.")

CHILD_AGE = 12
AGE_MAX = 80
WEIGHT_MAX = 300
AGE_LIMIT = int(input("Please enter your age: "))
keep_asking = True

while keep_asking == True:
    if AGE_LIMIT >= CHILD_AGE:
        print("Please take 2x500mg tablets.")
        keep_asking = False
    else:
        WEIGHT_LIMIT = int(input("Please enter your weight in KG: "))
        dosage = WEIGHT_LIMIT * 10
        print(f"The recommended dose for you is {dosage}mg.")
        keep_asking = False

if AGE_LIMIT < 0 or WEIGHT_LIMIT < 0 or AGE_LIMIT > 80 or WEIGHT_LIMIT > 300:
    print("That is not a valid input. Please enter a valid age and weight.")
    AGE_LIMIT = int(input("Please enter your age: "))
    WEIGHT_LIMIT = int(input("Please enter your weight in KG: "))
elif AGE_LIMIT > 9 and WEIGHT_LIMIT > 40:
    print("The recommended dose for you is 400mg.")
    keep_asking = False
elif AGE_LIMIT >= 12 and AGE_LIMIT <= 52:
    print("Take 2x500mg tablets.")
    keep_asking = False