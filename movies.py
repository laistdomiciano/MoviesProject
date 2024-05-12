import random
from movie_storage import *
from movies_web_generator import generate_website


API_KEY = '7804bbe4'

menu = ["Exit", "List movies", "Add movie", "Delete movie", "Update movie", "Stats", "Random movie", "Search movie", "Movies Sorted by Rating", "Generate website"]


def exit_program():
    """Closes the whole program"""
    print("You chose to Exit this program")
    print("Bye!")
    save_movies(movies)
    exit()


def stats():
  """ Show the analytics: Top-rated movies,
  least-rated movies etc movie from the movies database. """
  print("Stats")
  average_rating = sum(movie["rating"] for movie in movies.values()) / len(movies)
  median_rating = sorted(movie["rating"] for movie in movies.values())[len(movies) // 2]
  best_movie = max(movies, key=lambda x: movies[x]["rating"])
  worst_movie = min(movies, key=lambda x: movies[x]["rating"])
  print(f"Average rating: {average_rating}")
  print(f"Median rating: {median_rating}")
  print(f"Best movie: {best_movie} with rating {movies[best_movie]['rating']}")
  print(f"Worst movie: {worst_movie} with rating {movies[worst_movie]['rating']}")


def random_movie():
  """ Gives a random suggestion of movie from the database for the user"""
  print("Random Movie")
  print("You picked the random movie selector. The program will select a movie for you")
  movie, movie_details = random.choice(list(movies.items()))
  print(f"You should watch {movie}, it has {movie_details['rating']} rating.")


def search_movie():
  """ Searches a movie from the database with partial name info."""
  print("Search Movie")
  movie_search = input("Enter part of movie name: ").lower()
  found_movies = [movie for movie in movies.keys() if movie_search in movie.lower()]
  if found_movies:
    print("Movies found:")
    for movie in found_movies:
      print(movie)
  else:
    print("No movies found matching the search criteria.")


def movies_sorted_by_rating():
  """ Show from best to worse the movies from the data base"""
  print("Movies Sorted by Rating")
  sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
  for movie, movie_details in sorted_movies:
    print(f"{movie}: {movie_details['rating']}, {movie_details['year']}")


def choose_opt_dictionary(command):
  """ This program brings the menu options"""
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
      9: generate_website
  }
  if command in my_dict:
    my_dict[command]()  # No need to pass movies here
  else:
    print("Try Another Option")


# Menu loop
while True:
  movies = load_movies()
  print("\033[1;32m ********** My Movies Database **********\n")
  for index, item in enumerate(menu):
    print(index, item)
  user_choice = int(input("\033[1;36m Enter choice (0-9):\n"))
  choose_opt_dictionary(user_choice)
