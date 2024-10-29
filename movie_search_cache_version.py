import os
import pickle
from imdb import IMDb

CACHE_FILE = 'IMDB/movie_cache.pkl'


def load_cache():
    """Load cached data from a file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as cache_file:
            return pickle.load(cache_file)
    return {}


def save_cache(cache):
    """Save the cache to a file."""
    with open(CACHE_FILE, 'wb') as cache_file:
        pickle.dump(cache, cache_file)


def search_movies(search_string, cache):
    """Search for movies using the IMDb API and utilize cache."""
    if search_string in cache:
        print("Retrieving from cache...")
        return cache[search_string]

    print("Fetching from IMDb...")
    imdb_instance = IMDb()
    movies = imdb_instance.search_movie(search_string)

    movie_names = [movie['title'] for movie in movies]
    cache[search_string] = movie_names
    save_cache(cache)
    return movie_names


if __name__ == "__main__":
    cached_data = load_cache()  # Load cache at the start
    user_input = input("Enter a string to search for movies: ")
    results = search_movies(user_input, cached_data)

    if results:
        print("Movies found:")
        for movie_result in results:
            print(movie_result)
    else:
        print("No movies found.")
