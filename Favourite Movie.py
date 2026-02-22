'''This code asks the user what their favourite movie is three times and stores the movies in a list then prints it'''
#Creating a list
favourite_movie_list = []
print("Enter your 3 favourite movies of all time, in order from favourite to least")
for i in range(3):
    while True:
        movie = input("Enter name of movie: ")
        if movie == "":
            print("Don't enter a blank name.")
        else:       
            favourite_movie_list.append(movie)
            break
#Printing the list of movies
print(favourite_movie_list)
#Printing the user's 3 favourite movies in order with the 1,2,3
print("Your 3 favourite movies are...")
for i, event in enumerate(favourite_movie_list, start=1):
    print(f"{i}. {event}")