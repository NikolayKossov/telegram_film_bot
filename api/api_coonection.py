import requests
import urllib.parse
from config_data.config import RAPID_API_KEY

def search_film(name):
    # Ваш API ключ
    api_key = "NH65SAF-7M54JB8-KPRQ6DE-28HDAR2"

    # Название фильма, который вы хотите найти
    movie_name = str(name)

    # Кодируем название фильма для использования в URL
    encoded_movie_name = urllib.parse.quote(movie_name)

    # Формируем URL для запроса
    url = f"https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query={encoded_movie_name}"

    # Заголовки запроса
    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    # Выполняем GET запрос
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    # Преобразуем ответ в JSON объект
    movies = response.json()

    result_names = []
    result_years = []
    genres = []

    for film in movies.get("docs", []):
        if "name" in film:
            result_names.append(film["name"])
        else:
            result_names.append("N/A")

        if "year" in film:
            result_years.append(film["year"])
        else:
            result_years.append("N/A")

        if "genres" in film:
            genres.append([genre['name'] for genre in film["genres"]])
        else:
            genres.append([])

    combined_list = [f"{name} ({year}), Жанры: {', '.join(genre)}" for name, year, genre in
                     zip(result_names, result_years, genres)]

    return combined_list

