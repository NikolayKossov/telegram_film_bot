def get_film_list(films, genres_list):
    # Приводим жанры из genres_list к нижнему регистру для сравнения
    genres_list = set(genre.lower() for genre in genres_list)

    combined_list = []
    movies_id = []

    for film in films.get("docs", []):
        # Получаем жанры фильма в нижнем регистре
        film_genres = {genre['name'].lower() for genre in film.get("genres", [])}

        # Проверяем пересечение жанров фильма с genres_list
        if film_genres & genres_list:
            film_id = film.get("id", "N/A")
            film_name = film.get("name") or film.get("alternativeName", "N/A")
            film_year = film.get("year", "N/A")
            film_genre_names = [genre['name'] for genre in film.get("genres", [])]

            # Формируем описание фильма
            combined_list.append(f"{film_name} ({film_year}), Жанры: {', '.join(film_genre_names)}")
            movies_id.append(film_id)

    return combined_list, movies_id
