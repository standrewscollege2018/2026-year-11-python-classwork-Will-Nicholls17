'''To do list. This is a list that the user can things to and what time it needs to be done. There needs to be a constant opportunity to input things to the list and a button to see what is in the list'''

import random
import time
import sys



exit_button = ''
events = []

def add_event(event_list):
    print("-" * 30)
    print("Welcome to the event add screen")
    new_event = input("Please enter a new event > ")
    event_list.append(new_event)
    input("Press enter to continue...")
    time.sleep(1)
def view_events(event_list):
    count = 1
    print("-" * 30)
    for events in event_list:
        print(f"{count}-Event Name: {events}")
        count += 1
    print("-" * 30)
    input("Press Enter to continue...")
    time.sleep(1)
    print("-" * 30)
def select_random_event(event_list):
    print("-" * 30)
    count = 1
    num_of_event = int(input("How many events to select?: "))
    random_event = random.sample(event_list, num_of_event)
    for events in random_event:
        print(f"{count}-Event Name: {events}")
        count += 1
        print("Selecting the next event from the system...")
        time.sleep(1)
    print("-" * 30)
    input("Press Enter to continue...")
def shuffle_events(event_list):
    count = 1
    random.shuffle(event_list)
    for events in event_list:
        print(f"{count}-Event Name: {events}")
        count += 1
    print("-" * 30)
    input("Press Enter to continue...")
    time.sleep(1)
    print("-" * 30)
while True:
    print("\n****Welcome to your very own to do list****\n \n**If you want to close the program simply type '10' into the input key**\n")
    print("-" * 40)
    print("1-Add event\n2-View events\n3-Shuffle the events\n4-Select Random Event to do\n")
    print("-" * 30)
    section_choice = int(input("Choose an option > "))
    if section_choice == 1:
        add_event(events)
    elif section_choice == 2:
        view_events(events)
    elif section_choice == 3: 
        shuffle_events(events)
    elif section_choice == 4:
        select_random_event(events)
    elif section_choice == 10:
        sys.exit()
    else:
        print("Please enter a valid number.")
