from storage_json import StorageJson

# Create an instance of the storage class
storage = StorageJson('movies.json')

# List movies
print("Listing movies:")
print(storage.list_movies())

# Add a new movie
storage.add_movie('Inception', 2010, 8.8, 'http://poster.url/inception.jpg')

# List movies again to see the added movie
print("Listing movies after adding a new movie:")
print(storage.list_movies())

# Update an existing movie
storage.update_movie('Inception', 9.0)

# List movies again to see the updated rating
print("Listing movies after updating a movie:")
print(storage.list_movies())

# Delete a movie
storage.delete_movie('Inception')

# List movies again to see the deleted movie
print("Listing movies after deleting a movie:")
print(storage.list_movies())
