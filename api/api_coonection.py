import requests
import urllib.parse

from api import film_list

def search_film(cache):
    api_key = "NH65SAF-7M54JB8-KPRQ6DE-28HDAR2"
    name = cache["name"]
    genres = cache["genres"]
    pages = cache["pages"]

    movie_name = str(name)

    encoded_movie_name = urllib.parse.quote(movie_name)

    url = f"https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit={pages}&query={encoded_movie_name}"

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    films = response.json()
    films_list, films_id = film_list.get_film_list(films, genres)

    return films_list, films_id

