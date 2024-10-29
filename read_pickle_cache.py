import pickle

def read_cache():
    """Load and print cached data from a file."""
    try:
        with open('IMDB/movie_cache.pkl', 'rb') as cache_file:
            cache = pickle.load(cache_file)
            for search_string, movies in cache.items():
                print(f"Search string: '{search_string}'")
                print("Movies:")
                for movie in movies:
                    print(f" - {movie}")
                print()
    except FileNotFoundError:
        print("Cache file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_cache()
