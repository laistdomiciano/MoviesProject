import random
from storage_json import StorageJson
from movies_web_generator import generate_website

API_KEY = '7804bbe4'

menu = ["Exit", "List movies", "Add movie", "Delete movie", "Update movie", "Stats", "Random movie", "Search movie", "Movies Sorted by Rating", "Generate website"]

storage = StorageJson('movies.json')

class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def exit_program(self):
        """Closes the whole program"""
        print("You chose to Exit this program")
        print("Bye!")
        exit()

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        ...

    def stats(self):
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

    ...

    def _generate_website(self):
        ...

    def choose_opt_dictionary(self, command):
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

    def run(self):
      # Print menu
      while True:
          movies = self.load_movies()
          print("\033[1;32m ********** My Movies Database **********\n")
          for index, item in enumerate(menu):
              print(index, item)
          user_choice = int(input("\033[1;36m Enter choice (0-9):\n"))
          choose_opt_dictionary(user_choice)

      # Get use command

      # Execute command