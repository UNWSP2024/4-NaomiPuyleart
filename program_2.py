# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    add_movie = "y"
    movie_list = []
    tickets = 0
    total = 0

    while add_movie == "y":
        movie_title = input("Enter the movie title: ")
        movie_list.append(movie_title)
        tickets = int(input("Enter the number of tickets: "))
        total = total + tickets
        add_movie = input("Would you like to add another movie? Type 'y' if yes: ")
    ######################

    print("The movies you are going to see are", movie_list)
    print("The total number of tickets you are going to buy is", total)
    ######################


if __name__ == '__main__':
    main()