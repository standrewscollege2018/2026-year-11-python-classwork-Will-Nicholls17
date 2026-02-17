'''Cricket Player's Runs Calculator'''
keep_asking_games = True
while keep_asking_games:
    try:
        total_games = int(input("How many games did the cricket player play? > "))
        if total_games > 0:
            keep_asking_games = False
        elif total_games == 0:
            print("The cricket player did not play any games. Please enter a positive integer.")
        elif total_games > 500:
            print("That's a lot of games! Please enter a smaller positive integer.")
        elif total_games < 0:
            print("Please enter a positive integer.")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
total_runs = 0
for i in range(total_games):
    keep_asking = True
    while keep_asking == True:
        try:
            runs = int(input(f"Enter the runs scored in game {i + 1}: > "))
            if runs < 0:
                print("Runs cannot be negative. Please enter a valid number.")
            elif runs == 1000:
                print (f"There were {i} scores entered. The total number of runs is {total_runs} giving an average score of {total_runs / i:.2f}.")
                keep_asking = False
            else:
                total_runs += runs
                keep_asking = False
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
print("-" * 60 )
print(f"The total number of runs for {total_games} games is {total_runs}.")