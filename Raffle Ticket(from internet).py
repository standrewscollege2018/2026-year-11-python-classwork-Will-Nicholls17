import random
import time

users = list()
def add_user(users_list):
    print("-" * 30)
    print("Welcome to the User Addition Screen")
    new_user = input("Please enter a new user:")
    users_list.append(new_user)
    input("Press Enter to continue...")
def view_users(users_list):
    count = 1
    print("-" * 30)
    for user in users_list:
        print(f"{count}-User Name: {user}")
        count += 1
    print("-" * 30)
    input("Press Enter to continue...")
def select_random_users(users_list):
    print("-" * 30)
    count = 1
    num_of_users = int(input("How many users to select?: "))
    random_users = random.sample(users_list, num_of_users)
    for user in random_users:
        print(f"{count}-User Name: {user}")
        count += 1
        print("Selecting the next user from the system...")
        time.sleep(3)
    print("-" * 30)
    input("Press Enter to continue...")
def shuffle_users(users_list):
    count = 1
    random.shuffle(users_list)
    for user in users_list:
        print(f"{count}-User Name: {user}")
        count += 1
    print("-" * 30)
    input("Press Enter to continue...")
while True:
    print("****** Welcome to the Raffle Application ******")
    choice = int(input("1-Add User\n2-View Users\n3-Shuffle Users\n4-Select Random Users\n"))
    if choice == 1:
        add_user(users)
    elif choice == 2:
        view_users(users)
    elif choice == 3:
        shuffle_users(users)
    elif choice == 4:
        print("Calculating user selection...")
        time.sleep(2)
        select_random_users(users)
    else:
        print("Please make a valid choice")