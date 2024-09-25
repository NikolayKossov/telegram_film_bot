import requests
from . import film_list


def search_film_at_api_high_budget():
    api_key = "NH65SAF-7M54JB8-KPRQ6DE-28HDAR2"

    url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&sortField=budget.value&sortType=-1&lists=most-expensive"

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    films = response.json()
    films_list, films_id = film_list.get_film_list(films)

    return films_list, films_id
