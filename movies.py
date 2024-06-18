import random
from movie_storage import *
from movies_web_generator import generate_website

API_KEY = '7804bbe4'

menu = ["Exit", "List movies", "Add movie",
"Delete movie", "Update movie", "Stats", "Random movie", "Search movie",
"Movies Sorted by Rating", "Generate website"
]


def exit_program():
    """Closes the whole program"""
    print("You chose to Exit this program")
    print("Bye!")
    exit()


def add_movie():
    """ Adds a new movie by fetching its details from the OMDb API. """
    print("Add a New Movie")
    movie_name = input("Enter the name of the movie: ")
    try:
        add_movie_to_database(movie_name)
    except Exception as e:
        print(f"An error occurred: {e}")


def list_movies():
    """ Lists all movies from the database. """
    movies = load_movies()
    print("List of Movies:")
    for movie, movie_details in movies.items():
        rating = movie_details["rating"]
        year = movie_details["year"]
        print(f"{movie}: {rating}, {year}")


def delete_movie():
    """ Deletes a movie from the database. """
    print("Delete a movie")
    movie_to_delete = input("Enter the name of the movie to delete: ")
    try:
        delete_movie_from_database(movie_to_delete)
    except Exception as e:
        print(f"An error occurred: {e}")

def update_movie():
    pass


def stats():
    """ Shows statistics for the movies in the database. """
    print("Stats")
    movies = load_movies()
    average_rating = sum(movie["rating"] for movie in movies.values()) / len(movies)
    median_rating = sorted(movie["rating"] for movie in movies.values())[len(movies) // 2]
    best_movie = max(movies, key=lambda x: movies[x]["rating"])
    worst_movie = min(movies, key=lambda x: movies[x]["rating"])
    print(f"Average rating: {average_rating}")
    print(f"Median rating: {median_rating}")
    print(f"Best movie: {best_movie} with rating {movies[best_movie]['rating']}")
    print(f"Worst movie: {worst_movie} with rating {movies[worst_movie]['rating']}")


def random_movie():
    """ Gives a random movie suggestion from the database. """
    print("Random Movie")
    print("You picked the random movie selector. The program will select a movie for you")
    movies = load_movies()
    movie, movie_details = random.choice(list(movies.items()))
    print(f"You should watch {movie}, it has {movie_details['rating']} rating.")


def search_movie():
    """ Searches for a movie in the database by partial name. """
    print("Search Movie")
    movie_search = input("Enter part of the movie name: ").lower()
    movies = load_movies()
    found_movies = [movie for movie in movies.keys() if movie_search in movie.lower()]
    if found_movies:
        print("Movies found:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found matching the search criteria.")


def movies_sorted_by_rating():
    """ Shows movies sorted by rating in descending order. """
    print("Movies Sorted by Rating")
    movies = load_movies()
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for movie, movie_details in sorted_movies:
        print(f"{movie}: {movie_details['rating']}, {movie_details['year']}")


def choose_opt_dictionary(command):
    """ Maps user command to the corresponding function. """
    my_dict = {
        0: exit_program,
        1: list_movies,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: stats,
        6: random_movie,
        7: search_movie,
        8: movies_sorted_by_rating,
        9: lambda: generate_website(load_movies())  # Pass movies to generate_website
    }
    if command in my_dict:
        my_dict[command]()
    else:
        print("Try Another Option")


def main():
    """ Main function to run the movie database program. """
    while True:
        print("\033[1;32m ********** My Movies Database **********\n")
        for index, item in enumerate(menu):
            print(index, item)
        user_choice = int(input("\033[1;36m Enter choice (0-9):\n"))
        choose_opt_dictionary(user_choice)

if __name__ == "__main__":
    main()
