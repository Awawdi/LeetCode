from flask import Flask, render_template, request
import os
import pickle
from imdb import IMDb

app = Flask(__name__)

CACHE_FILE = 'movie_cache.pkl'


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
        return cache[search_string]

    imdb_instance = IMDb()
    movies = imdb_instance.search_movie(search_string)

    movie_names = [movie['title'] for movie in movies]
    cache[search_string] = movie_names
    save_cache(cache)
    return movie_names


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    search_string = ""

    if request.method == 'POST':
        search_string = request.form['search']
        cache = load_cache()
        results = search_movies(search_string, cache)

    return render_template('index.html', search_string=search_string, results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
