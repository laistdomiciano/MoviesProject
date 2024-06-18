import json
import os
import requests

API_KEY = '7804bbe4'
movies_database = []

def load_movies():
    """ Loads movies from the JSON file. """
    if os.path.exists("movies.json"):
        with open("movies.json", "r") as fileobj:
            movies = json.loads(fileobj.read())
    else:
        movies = {}
    return movies

def save_movies(movies):
    """ Saves the updated movies to the JSON file. """
    with open("movies.json", "w") as fileobj:
        json.dump(movies, fileobj)


def add_movie_to_database(movie_name):
    """ Adds a movie to the movies database by fetching its information from OMDb API. """
    movies = load_movies()
    url_movie = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}'
    response = requests.get(url_movie)
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data.get('Response') == 'True':
            title = movie_data.get('Title')
            year = movie_data.get('Year')
            rating = float(movie_data.get('imdbRating'))
            poster_url = movie_data.get('Poster')

            if title not in movies:
                movies[title] = {
                    'year': year,
                    'rating': rating,
                    'poster_url': poster_url
                }
                save_movies(movies)
                print(f"Added '{title}' to the database.")
            else:
                print(f"Movie '{title}' already exists in the database.")
        else:
            print(f"Movie '{movie_name}' not found in the database. Try another movie.")
    else:
        print("Error: Unable to access the OMDb API. Please check your internet connection and try again.")


def delete_movie_from_database(movie_to_delete):
    """ Deletes a movie from the movies database. """
    movies = load_movies()
    if movie_to_delete in movies:
        removed_movie = movies.pop(movie_to_delete)
        save_movies(movies)
        print(f"Movie '{movie_to_delete}' was deleted successfully!")
    else:
        print(f"Movie '{movie_to_delete}' not found in the database. Please try again.")


def update_movie():
  """ Updates a movie from the movies database.
  Loads the information from the JSON file, updates the movie,
  and saves it. """
  movies = load_movies()
  print("Update Movie")
  movie_to_update = input("What Movie you want to update:")
  if movie_to_update in movies:
    new_rating = float(input("Enter the new rating of the movie: "))
    movies[movie_to_update]["rating"] = new_rating
    save_movies()
    print(f"Movie '{movie_to_update}' updated successfully!")
  else:
    print(f"Movie '{movie_to_update}' not found in the database. Please try again.")
