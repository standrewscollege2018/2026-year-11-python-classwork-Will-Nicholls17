'''Random number, trying to get it to do a desired number (It's very rare)'''
import random
number = 0
while True:
    random_int = random.randint(0, 10000000000)
    print(f"{random_int}")
    number += 1
    if random_int <= 1000:
        print(f"It took this many tries to get that number: {number}")
        break        