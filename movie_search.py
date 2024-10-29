from imdb import IMDb


def search_movies(search_string):
    # Create an instance of the IMDb class
    ia = IMDb()

    # Search for movies containing the search string
    movies = ia.search_movie(search_string)

    # Retrieve and print movie names
    movie_names = [movie['title'] for movie in movies]

    return movie_names


if __name__ == "__main__":
    user_input = input("Enter a string to search for movies: ")
    results = search_movies(user_input)

    if results:
        print("Movies found:")
        for movie_result in results:
            print(movie_result)
    else:
        print("No movies found.")
