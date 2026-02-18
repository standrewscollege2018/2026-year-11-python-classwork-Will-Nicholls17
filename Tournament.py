'''Tournament points calculation system'''

import random
import textwrap
import time
import sys

opponents = []
opponents_temporary = []

print("Welcome to the Super Tournament Points Calculation system!")

keep_asking_entire_team_name_input = True
while keep_asking_entire_team_name_input == True:
    #This section is for getting the team name input and validating it. It also gives the user the option to capitalize the first letter of their team name or not.
    get_team_name_input = True
    while get_team_name_input == True:
        name_of_our_team_error_catch = True
        while name_of_our_team_error_catch == True:
            name_of_our_team = input("What is the name of your team? > ")
            if name_of_our_team == "":
                print("Invalid team name. Please enter a non-empty name.")
                get_team_name_input = True
            else:
                name_of_our_team_error_catch = False

        keep_asking_strip_input = True
        while keep_asking_strip_input == True:
            is_stripped = input("Do you want to strip your team name of any leading or trailing whitespace? (yes/no) > ").lower()
            if is_stripped == "yes":
                name_of_our_team = name_of_our_team.strip()
                keep_asking_strip_input = False
            elif is_stripped == "no":
                name_of_our_team = name_of_our_team
                keep_asking_strip_input = False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                keep_asking_strip_input = True
        keep_asking_capitalize_input = True
        while keep_asking_capitalize_input == True:
            is_capitalized = input("Do you want the first letter of your team name to be capitalized? (This removes all capital letters other than the first letter) (yes/no) > ").lower()
            if is_capitalized == "yes":
                name_of_our_team = name_of_our_team.capitalize()
                keep_asking_capitalize_input = False
            elif is_capitalized == "no":
                name_of_our_team = name_of_our_team
                keep_asking_capitalize_input = False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                keep_asking_capitalize_input = True
        break


    #This section is for getting the number of teams in the tournament and validating it. It also gets the names of the opponents and validates them. The user also has the option to reset the opponents names if they want to.

    keep_asking = True
    while keep_asking == True:
        get_number_team_input = True
        while get_number_team_input == True:
            try:
                number_team = int(input("How many other teams are in the tournament? (you have to write out each opponent's name) > "))
                if number_team < 1:
                    print("Invalid number of people. Please enter a number greater than 0.")
                elif number_team > 25:
                    print("Invalid number of people. Please enter a number less than or equal to 25.")
                else:
                    get_number_team_input = False
            except ValueError: 
                print("Invalid. Please enter an integer")

        #This section is for getting the names of the opponents and validating them. The user also has the option to reset the opponents names if they want to.

        team_input = True
        while team_input == True:
            for i in range(1, int(number_team) + 1):
                keep_asking_opponent_name = True
                while keep_asking_opponent_name == True:
                    opponent_name = input("Enter the name of opponent " + str(i) + ": ")
                    if opponent_name == "":
                        print("Invalid team name. Please enter a non-empty name.")
                        keep_asking_opponent_name = True
                    elif opponent_name == name_of_our_team:
                        print("Invalid team name. Opponent name cannot be the same as your team name.")
                        keep_asking_opponent_name = True
                    elif opponent_name in opponents:
                        print("Invalid team name. Opponent name cannot be the same as another opponent's name.")
                        keep_asking_opponent_name = True
                    else:                                
                        keep_asking_opponent_name = False
                keep_asking_opponenent_error_catcher = True
                while keep_asking_opponenent_error_catcher == True:

                    keep_asking_opponent_name_strip_input = True
                    while keep_asking_opponent_name_strip_input == True:
                        opponent_name_stripped_input = input("Do you want to strip the opponent's name of any leading or trailing whitespace? (yes/no) > ").lower()
                        if opponent_name_stripped_input == "yes":
                            opponent_name = opponent_name.strip()
                            keep_asking_opponent_name_strip_input = False                        
                        elif opponent_name_stripped_input == "no":
                            opponent_name = opponent_name
                            keep_asking_opponent_name_strip_input = False
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                            keep_asking_opponent_name_strip_input = True
                            keep_asking_opponenent_error_catcher = False      

                    keep_asking_opponent_name_capitalized_input = True
                    while keep_asking_opponent_name_capitalized_input == True:                        
                        opponent_name_capitalized_input = input("Do you want the first letter of the opponent's name to be capitalized? (This removes all capital letters other than the first letter) (yes/no) > ").lower()
                        if opponent_name_capitalized_input == "yes":
                            opponent_name = opponent_name.capitalize()
                            keep_asking_opponent_name_capitalized_input = False
                            keep_asking_opponenent_error_catcher = False
                        elif opponent_name_capitalized_input == "no":
                            keep_asking_opponent_name_capitalized_input = False
                            keep_asking_opponenent_error_catcher = False
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                            keep_asking_opponent_name_capitalized_input = True
                opponents.append(opponent_name)
                print(f"Opponent {i} is {opponent_name}")
                

            #This section is for askingt the user if they want to reset the opponents names or not.

            team_input_keep_asking = True
            while team_input_keep_asking == True:
                team_name_input = input("Do you want to enter the opponents again? (resets the opponents names) (yes/no) > ")
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
                    team_input_checker = input("Invalid input. Please enter 'yes' or 'no' > ")
                    if team_input_checker == "yes":
                        team_input = True
                        team_input_keep_asking = False
                        opponents.clear()
                    elif team_input_checker == "no":
                        print("-" * 60)
                        print("Great! Let's move on to the next step of the tournament, the game!")
                        team_input = False 
                        team_input_keep_asking = False
                    
        #This section is for explaining the game and how the points are awarded. It also displays the opponents in the tournament.

        print("Opponents in the tournament:")
        print(f"{name_of_our_team}, {', '.join(opponents)}")
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
        total_opponents_points = []
        temporary_opponents_points = []
        away_team_points = 0
        total_points = 0

        #This section is for the game itself. It randomly selects an opponent from the opponents list and asks the user to input the points scored by both teams. It then calculates the points awarded to the user's team and the opponent's team based on the points scored and displays the results of the game. This process is repeated for each opponent in the tournament.

        for i in range(1, int(number_team) + 1):
            opponent_name = random.choice(opponents)
            print(f"Game results vs {opponent_name}")
            keep_asking_game = True
            while keep_asking_game == True:
                try:
                    home_team_points = int(input(f"How many points did {name_of_our_team} score against {opponent_name}? > "))
                    keep_asking_game = False
                    if home_team_points < 0:
                        print("Invalid input. Please enter a non-negative integer.")
                        keep_asking_game = True
                    elif home_team_points > 300:
                        print("Invalid input. Please enter a number between 0 and 300.")
                        keep_asking_game = True
                except ValueError:
                    print("Invalid input. Please enter integers only.")

            #This section is for validating the points scored by the opponent team. It also calculates the points awarded to both teams based on the points scored and displays the results of the game. This process is repeated for each opponent in the tournament.

            keep_asking_score_checker = True
            while keep_asking_score_checker == True:
                try:
                    away_team_points = int(input(f"How many points did {opponent_name} score against {name_of_our_team}? > "))
                    keep_asking_score_checker = False
                    if away_team_points < 0:
                        print("Invalid input. Please enter a non-negative integer.")  
                        keep_asking_score_checker = True 
                    elif away_team_points > 300:
                        print("Invalid input. Please enter a number between 0 and 300.")
                        keep_asking_score_checker = True 
                except ValueError:
                    print("Invalid input. Please enter integers only.")
            if home_team_points > away_team_points:
                winner = name_of_our_team
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
            wrapped_text1 = textwrap.fill(f"The score for the game between {name_of_our_team} and {opponent_name} was {home_team_points} - {away_team_points}. The winner is {winner}! Points awarded to {name_of_our_team}: {points} and points awarded to {opponent_name}: {temporary_opponents_points}", width=30)
            print(wrapped_text1)
            opponents.remove(opponent_name)
            print("-" * 60)
        print("-" * 60)
        time.sleep(3)
        print(f"{name_of_our_team} finished the competition with: {total_points} total point(s).") 
        time.sleep(2)

        #This section is for displaying the total points of each opponent and determining the winner of the tournament based on the total points of each team. It also gives the user the option to play the tournament again or not.

        for i in range(1, int(number_team) + 1):
            opponent_name = opponents_temporary[i - 1]
            print(f"{opponent_name} finished the competition with: {total_opponents_points[i - 1]} total point(s).")
            time.sleep(2)
        
        winner1 = max(total_points, max(total_opponents_points))
        if winner1 == total_points:
            print(f"The winner of the tournament is: {name_of_our_team}")
        elif total_opponents_points and name_of_our_team == total_points:
            print(f"This tournament is a draw between {opponents_temporary} and {name_of_our_team}")
        else:
            for i in range(len(total_opponents_points)):
                if total_opponents_points[i] == winner1:
                    print(f"The winner of the tournament is: {opponents_temporary[i]}")
                    break
        time.sleep(2)

        play_tournament_again_input = input("Do you want to play the tournament again? (yes/no) > ").lower()
        if play_tournament_again_input == "yes":
            print("-" * 60)
            print("Great! Let's play the tournament again!")
        elif play_tournament_again_input == "no":
            print("Thank you for playing the Super Tournament Points Calculation system! Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

        
        time.sleep(3)
        keep_asking_full_game = True
        while keep_asking_full_game == True:
            keep_asking_full_game_input = input("Do you want to play the tournament again with all same names? (yes/no) > ").lower()
            if keep_asking_full_game_input == "yes":
                print("Great! Let's play the tournament again with all the same names!")
                keep_asking = False
                keep_asking_full_game = False
                keep_asking_entire_team_name_input = True
            elif keep_asking_full_game_input == "no":
                play_new_names_input = input("Do you want to play the tournament again with the same team name? (yes/no) > ").lower()
                if play_new_names_input == "yes":
                    play_new_opponents_names_input = input("Do you want to play the tournament again with the same opponents names? (yes/no) > ").lower()
                    if play_new_opponents_names_input == "yes":
                        print("Great! Let's play the tournament again with the same team name but new opponents names!")
                        keep_asking = True
                        keep_asking_full_game = False
                        keep_asking_entire_team_name_input = True
                    elif play_new_opponents_names_input == "no":
                        print("Great! Let's play the tournament again with the same team name but new opponents names!")
                        keep_asking = False
                        keep_asking_full_game = False
                        keep_asking_entire_team_name_input = True
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                elif play_new_names_input == "no":
                    print("Great! Let's play the tournament again with new team name and new opponents names!")
                    keep_asking_entire_team_name_input = True
                    keep_asking = False
                    keep_asking_full_game = False
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")