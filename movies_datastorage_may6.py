import json
import requests


def load_movies():
  """ Opens the json file """
  with open("movies.json", "r") as fileobj:
    movies = json.loads(fileobj.read())
  return movies

movies = load_movies()

def save_movies():
  """ Updates the json file """
  with open("movies.json", "w") as fileobj:
    json.dump(movies, fileobj)


def list_movies():
  """ Prints a list of movies with their ratings and years """
  print("List of Movies:")
  for movie, movie_details in movies.items():
    rating = movie_details["rating"]
    year = movie_details["year"]
    print(f"{movie}: {rating}, {year}")


def add_movie():
    """ Adds a movie to the movies database """
    title = input("Enter new movie name: ")
    if title in movies:
        print(f"Movie {title} already exists!")
        return
    rating = float(input("Enter the rating of the movie: "))
    year = int(input("Enter the year of the movie: "))
    movies[title] = {'year': year, 'rating': rating}
    save_movies()
    print(f"Movie {title} successfully added")


def delete_movie():
  """ Deletes a movie from the movies database. Loads the
  information from the JSON file, deletes the movie, and saves it."""
  print("Delete a movie")
  movie_to_delete = input("What Movie you want to delete:")
  if movie_to_delete in movies:
    removed_movie = movies.pop(movie_to_delete)
    print(f" Movie '{movie_to_delete}' was deleted successfully!")
    save_movies()
  else:
    print(f"Movie '{movie_to_delete}' not found in the database. Please try again.")


def update_movie():
  """ Updates a movie from the movies database.
  Loads the information from the JSON file, updates the movie,
  and saves it. """
  print("Update Movie")
  movie_to_update = input("What Movie you want to update:")
  if movie_to_update in movies:
    new_rating = float(input("Enter the new rating of the movie: "))
    movies[movie_to_update]["rating"] = new_rating
    save_movies()
    print(f"Movie '{movie_to_update}' updated successfully!")
  else:
    print(f"Movie '{movie_to_update}' not found in the database. Please try again.")
