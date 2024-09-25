import urllib

import requests
from . import filter_by_rating


def movie_by_rating_buffer(cache):
    api_key = "NH65SAF-7M54JB8-KPRQ6DE-28HDAR2"
    name = cache["name"]
    rating = cache["rating"]
    pages = cache["pages"]

    movie_name = str(name)

    encoded_movie_name = urllib.parse.quote(movie_name)

    url = f"https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit={pages}&query={encoded_movie_name}"

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.get(url, headers=headers)
    films = response.json()
    films_list = filter_by_rating.get_film_list(films, rating)

    return films_list
