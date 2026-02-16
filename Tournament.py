'''Tournament points calculation system'''

import random
import textwrap
import time

opponents = list() 
opponents_temporary = list()

print("Welcome to the Super Tournament Points Calculation system!")

NAME_OF_OUR_TEAM_NOT_STRIPPED = input("What is the name of your team? > ")
NAME_OF_OUR_TEAM = NAME_OF_OUR_TEAM_NOT_STRIPPED.strip().capitalize()
NAME_OF_OUR_TEAM_INPUT = True
while NAME_OF_OUR_TEAM_INPUT == True:
    if NAME_OF_OUR_TEAM == "":
        print("Invalid team name. Please enter a non-empty name.")
        NAME_OF_OUR_TEAM = input("What is the name of your team? >")
    else:
        NAME_OF_OUR_TEAM_INPUT = False

keep_asking = True
while keep_asking == True:
    team_input1 = True
    while team_input1 == True:
        try:
            team = int(input("How many other teams are in the tournament? (you have to write out each opponent's name) > "))
            if team < 1:
                print("Invalid number of people. Please enter a number greater than 0.")
            elif team > 25:
                print("Invalid number of people. Please enter a number less than or equal to 25.")
            else:
                team_input1 = False
        except ValueError: 
            print("Invalid. Please enter an integer")

    team_input = True
    while team_input == True:
        for i in range(1, int(team) + 1):
                keep_asking5 = True
                while keep_asking5 == True:
                    opponent_name_not_stripped = input("Enter the name of opponent " + str(i) + ": ")
                    opponent_name = opponent_name_not_stripped.strip().capitalize()
                    if opponent_name == "":
                        print("Invalid team name. Please enter a non-empty name.")
                    elif opponent_name == NAME_OF_OUR_TEAM:
                        print("Invalid team name. Opponent name cannot be the same as your team name.")
                    elif opponent_name in opponents:
                        print("Invalid team name. Opponent name cannot be the same as another opponent's name.")
                    else:
                        keep_asking5 = False
                opponents.append(opponent_name)
                print(f"Opponent {i} is {opponent_name}")

        team_name_input = input("Do you want to enter the opponents again? (resets the opponents names) (yes/no) > ")
        team_input_keep_asking = True
        while team_input_keep_asking == True:
            if team_name_input == "yes":
                team_input = True
                team_input_keep_asking = False
                opponents.clear()
            elif team_name_input == "no":
                print("-" * 60)
                print("Great! Let's move on to the next step of the tournament, the game!")
                team_input = False 
                team_input_keep_asking = False
            else:
                team_input_2 = input("Invalid input. Please enter 'yes' or 'no' > ")
                if team_input_2 == "yes":
                    team_input = True
                    team_input_keep_asking = False
                    opponents.clear()
                elif team_input_2 == "no":
                    print("-" * 60)
                    print("Great! Let's move on to the next step of the tournament, the game!")
                    team_input = False 
                    team_input_keep_asking = False

    print("Opponents in the tournament:")
    print(f"{NAME_OF_OUR_TEAM}, {', '.join(opponents)}")
    print("-" * 60)
    time.sleep(2)
    print("** Game **")
    wrapped_text = textwrap.fill("In the game, you will be playing against each opponent. You will be awarded points based on your performance in the game. The winner is whoever has the most amount of points at the end of the tournament. The points are as follows:", width=30)
    print(wrapped_text)
    print("Win: 3 points")
    print("Draw: 2 points")
    print("Lose: 1 point")
    wrapped_text2 = textwrap.fill("After playing against all the opponents, your total points will be calculated and displayed. Good luck in the tournament!", width=30)
    print(wrapped_text2)
    print("-" * 60)
    time.sleep(12)

    opponents_temporary = opponents.copy()
    
    total_opponents_points = list()
    temporary_opponents_points = list()
    away_team_points = 0
    total_points = 0

    for i in range(1, int(team) + 1):
        opponent_name = random.choice(opponents)
        print(f"Game results vs {opponent_name}")
        keep_asking6 = True
        while keep_asking6 == True:
            try:
                home_team_points = int(input(f"How many points did {NAME_OF_OUR_TEAM} score against {opponent_name}? > "))
                keep_asking6 = False
                if home_team_points < 0:
                    print("Invalid input. Please enter a non-negative integer.")
                    keep_asking6 = True
                elif home_team_points > 300:
                    print("Invalid input. Please enter a number between 0 and 300.")
                    keep_asking6 = True
            except ValueError:
                print("Invalid input. Please enter integers only.")
        keep_asking7 = True
        while keep_asking7 == True:
            try:
                away_team_points = int(input(f"How many points did {opponent_name} score against {NAME_OF_OUR_TEAM}? > "))
                keep_asking7 = False
                if away_team_points < 0:
                    print("Invalid input. Please enter a non-negative integer.")  
                    keep_asking7 = True 
                elif away_team_points > 300:
                    print("Invalid input. Please enter a number between 0 and 300.")
                    keep_asking7 = True 
            except ValueError:
                print("Invalid input. Please enter integers only.")
        if home_team_points > away_team_points:
            winner = NAME_OF_OUR_TEAM
            points = +3
            temporary_opponents_points = +1
        elif home_team_points == away_team_points:
            points = +2
            temporary_opponents_points = +2
            winner = "Draw"
        elif home_team_points < away_team_points:
            winner = opponent_name
            points = +1
            temporary_opponents_points = +3
        total_points += points
        total_opponents_points.append(temporary_opponents_points)
        wrapped_text1 = textwrap.fill(f"The score for the game between {NAME_OF_OUR_TEAM} and {opponent_name} was {home_team_points} - {away_team_points}. The winner is {winner}! Points awarded to {NAME_OF_OUR_TEAM}: {points} and points awarded to {opponent_name}: {temporary_opponents_points}", width=30)
        print(wrapped_text1)
        opponents.remove(opponent_name)
        print("-" * 60)
    print("-" * 60)
    time.sleep(3)
    print(f"{NAME_OF_OUR_TEAM} finished the competition with: {total_points} total point(s).") 
    time.sleep(2)

    for i in range(1, int(team) + 1):
        opponent_name = opponents_temporary[i - 1]
        print(f"{opponent_name} finished the competition with: {total_opponents_points[i - 1]} total point(s).")
        time.sleep(2)
    
    winner1 = max(total_points, max(total_opponents_points))
    if winner1 == total_points:
        print(f"The winner of the tournament is: {NAME_OF_OUR_TEAM}")
    else:
        for i in range(len(total_opponents_points)):
            if total_opponents_points[i] == winner1:
                print(f"The winner of the tournament is: {opponents_temporary[i]}")
                break
    time.sleep(2)
    keep_asking2_input = True
    while keep_asking2_input == True:
        keep_asking2 = input("Do you want to play the tournament again? (yes/no) > ").lower()
        if keep_asking2 == "yes":
            opponents.clear()
            keep_asking = True
            keep_asking2_input = False
        elif keep_asking2 == "no":
            print("Thank you for playing the Super Tournament Points Calculation system! Goodbye!")
            keep_asking = False
            keep_asking2_input = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")