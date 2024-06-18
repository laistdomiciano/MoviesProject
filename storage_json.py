import json
import os
import requests
from istorage import IStorage

API_KEY = '7804bbe4'

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self.load_movies()

    def load_movies(self):
        """Loads movies from a JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as fileobj:
                return json.loads(fileobj.read())
        return {}

    def save_movies(self):
        """Saves movies to a JSON file."""
        with open(self.file_path, "w") as fileobj:
            json.dump(self.movies, fileobj)

    def list_movies(self):
        """Returns a dictionary of dictionaries that contains the movies information in the database."""
        return self.movies

    def add_movie(self, title, year, rating, poster):
        """Adds a movie to the movies database."""
        url_movie = f'http://www.omdbapi.com/?apikey={API_KEY}&t={title}'
        response = requests.get(url_movie)
        movie_data = response.json()
        if movie_data.get('Response') == 'True':
            title = movie_data.get('Title')
            year = movie_data.get('Year')
            rating = float(movie_data.get('imdbRating'))
            poster_url = movie_data.get('Poster')
            self.movies[title] = {
                'year': year,
                'rating': rating,
                'poster_url': poster_url
            }
            self.save_movies()
            print(f"Added '{title}' to the database.")
        else:
            print(f"Movie '{title}' not found in the database. Try another movie.")

    def delete_movie(self, title):
        """Deletes a movie from the movies database."""
        if title in self.movies:
            del self.movies[title]
            self.save_movies()
            print(f"Movie '{title}' was deleted successfully!")
        else:
            print(f"Movie '{title}' not found in the database.")

    def update_movie(self, title, rating):
        """Updates a movie in the movies database."""
        if title in self.movies:
            self.movies[title]['rating'] = rating
            self.save_movies()
            print(f"Movie '{title}' updated successfully!")
        else:
            print(f"Movie '{title}' not found in the database.")