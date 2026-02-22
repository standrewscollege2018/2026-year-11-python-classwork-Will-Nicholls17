'''To do list. This is a list that the user can things to and what time it needs to be done. There needs to be a constant opportunity to input things to the list and a button to see what is in the list'''


import random
import time

def add_event(events):
    print("-" * 30)
    print("Add Event (type 'cancel' to stop)")
    while True:
        event = input("Enter new event: ")
        if event == "":
            print("Please enter a non-empty event.")
        elif event.lower() == "cancel":
            break
        elif event in events:
            print("This event already exists.")
        else:
            events.append(event)
            print(f"'{event}' added successfully!")
            break
    input("Press Enter to continue...")
    time.sleep(1)

def view_events(events):
    print("-" * 30)
    print("Your Events:\n")
    if not events:
        print("No events yet!")
    else:
        for i, event in enumerate(events, start=1):
            print(f"{i}. {event}")
    input("Press Enter to continue...")
    time.sleep(1)

def shuffle_events(events):
    print("-" * 30)
    if not events:
        print("No events to shuffle!")
    else:
        random.shuffle(events)
        print("Events shuffled successfully!")
    input("Press Enter to continue...")
    time.sleep(1)

def random_event(events):
    print("-" * 30)
    if not events:
        print("No events to choose from!")
    else:
        chosen = random.choice(events)
        print(f"You have been chosen to do: {chosen}")
    input("Press Enter to continue...")
    time.sleep(1)

def remove_event(events):
    print("-" * 30)
    if not events:
        print("No events to delete!")
        input("Press Enter to continue...")
        return
    print("Current Events:")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event}")
    try:
        num = int(input("Enter number of event to delete: "))
        if 1 <= num <= len(events):
            removed = events.pop(num - 1)
            print(f"'{removed}' removed successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")
    input("Press Enter to continue...")
    time.sleep(1)

def main():
    event_list = []  # our central to-do list

    while True:
        print("\n**** Welcome to Your To-Do List ****")
        print("Type '6' at any menu to exit\n")
        print("-" * 40)
        print("1 - Add Event")
        print("2 - View Events")
        print("3 - Shuffle Events")
        print("4 - Random Event")
        print("5 - Remove Event")
        print("-" * 30)

        try:
            choice = int(input("Choose an option > "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_event(event_list)
        elif choice == 2:
            view_events(event_list)
        elif choice == 3:
            shuffle_events(event_list)
        elif choice == 4:
            random_event(event_list)
        elif choice == 5:
            remove_event(event_list)
        elif choice == 6:
            print("Thanks for using the To-Do List!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

def load_events(filename):
    """Load events from a file into a list."""
    try:
        with open(filename, "r") as f:
            events = [line.strip() for line in f if line.strip()]
        return events
    except FileNotFoundError:
        # File doesn’t exist yet → start with empty list
        return []

def save_events(filename, events):
    """Save the list of events to a file."""
    with open(filename, "w") as f:
        for event in events:
            f.write(event + "\n")

