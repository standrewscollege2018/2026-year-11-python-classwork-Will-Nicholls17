'''To do list. This is a list that the user can things to and what time it needs to be done. There needs to be a constant opportunity to input things to the list and a button to see what is in the list'''

import random
import time
import sys

event_list = []

while True:
    print("\n****Welcome to your very own to do list****\n \n**If you want to close the program simply type '6' into the input key**\n")
    print("-" * 40)
    print("1-Add event\n2-View events\n3-Shuffle the events\n4-Select Random Event to do\n5-Remove Event\n")
    print("-" * 30)
    while True:
        try:
            section_choice = int(input("Choose an option > "))
            if section_choice < 0:
                print("Please enter a non-negative inter")
            elif section_choice >= 7:
                print("Please don't enter a number higher than the options given")
            else:
                break
        except ValueError:
            print("Please enter an integer")
    if section_choice == 1:
        print("-" * 30)
        print("Welcome to the event add screen (If you want to cancel the add new event, write 'cancel')")
        while True:
            event = input("Please enter a new event > ")
            if event == '':
                print("Please enter a non empty event")
            elif event == 'cancel':
                break
            elif event in event_list:
                print("You've already chosen that as one of your events.")
            else:
                event_list.append(event)
                break
        print()
        input("Press enter to continue...")
        time.sleep(1)
    elif section_choice == 2:
        print("-" * 30)
        print("Welcome to the event show screen.\n")
        if not event_list:
            print("No events in your list yet!")
        else:
            for i, event in enumerate(event_list, start=1):
                print(f"{i}. {event}")
        print("-" * 30)
        input("Press Enter to continue...")
        time.sleep(1)
        print("-" * 30)
    elif section_choice == 3:
        print("-" * 30)
        print("Welcome to the event random change screen.")
        if not event_list:
            print("No events to shuffle!")
        else:
            random.shuffle(event_list)
            time.sleep(1)
            print("Events shuffled successfully!")
        print("-" * 30)
        input("Press Enter to continue...")
    elif section_choice == 4:
        print("-" * 30)
        print("Welcome to the random event to do page.")
        if not event_list:
            print("You don't have any events yet!")
        else:
            random_event = random.choice(event_list)
            print(f"You have been chosen to do: {random_event}")
        print("-" * 30)
        input("Press Enter to continue...")
        time.sleep(1)
        print("-" * 30)
    elif section_choice == 5:
        print("-" * 30)
        print("Welcome to the event remove screen\n")
        if not event_list:
            print("No tasks available to delete!")
            input("Press enter to continue")
            continue
        print("\nCurrent events: ")
        for i, task in enumerate(event_list, start = 1):
            print(f"{i}. {task}")

        try:
            delete_event_num = int(input("Enter a task to delete: "))
            if 1 <= delete_event_num <= len(event_list):
                removed_event = event_list.pop(delete_event_num - 1)
                print(f"Task '{removed_event}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")
        input("Press Enter to continue...")
        time.sleep(1)
        print("-" * 30)
    elif section_choice == 6:
        print("Thank you for my To - Do list!")
        sys.exit()
    else:
        print("Please enter a valid number.")

    