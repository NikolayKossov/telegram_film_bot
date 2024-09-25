import requests
from io import BytesIO
from PIL import Image


def search_film_at_api(id):
    api_key = "NH65SAF-7M54JB8-KPRQ6DE-28HDAR2"
    url = f"https://api.kinopoisk.dev/v1.4/movie/{id}"

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key,
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    movie = response.json()
    name = movie.get("name", None)
    description = movie.get("description", None)
    rating = movie.get("rating", {})
    imdb_rating = rating.get("imdb", None)
    year = movie.get("year", None)
    ageRating = movie.get("ageRating", None)
    genres = [genre.get('name') for genre in movie.get("genres", [])]
    poster = movie.get("poster", {})
    poster_url = poster.get("url", None)

    image_bytes = None
    if poster_url:
        photo_response = requests.get(poster_url)
        photo_response.raise_for_status()
        image = Image.open(BytesIO(photo_response.content))
        image.thumbnail((1024, 1024), Image.LANCZOS)  # Уменьшение размера изображения
        image_bytes = BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)

    all_information_about_film = (
        f"{name} ({year})\n"
        f"{description}\n"
        f"Рейтинг IMDb: {imdb_rating}\n"
        f"Возраст: {ageRating}+ \n"
        f"Жанры: {', '.join(genres)}"
    )

    return all_information_about_film, image_bytes
