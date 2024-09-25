def get_film_list(films, user_rating):
    user_rating = int(user_rating[0])
    movies_id = []
    result_names = []
    result_years = []
    genres = []
    imdb_ratings = []

    for film in films.get("docs", []):
        if "id" in film:
            movies_id.append(film["id"])
        else:
            movies_id.append("N/A")

        if "name" in film:
            result_names.append(film["name"])
        else:
            result_names.append("N/A")  # Исправлено на result_names

        if "year" in film:
            result_years.append(film["year"])
        else:
            result_years.append("N/A")

        if "genres" in film:
            genres.append([genre['name'] for genre in film["genres"]])
        else:
            genres.append([])

        # Добавляем рейтинг IMDb
        if "rating" in film and "imdb" in film["rating"]:
            imdb_rating = film["rating"]["imdb"]
        else:
            imdb_rating = 0  # Если рейтинг отсутствует, ставим 0

        # Добавляем фильмы, которые имеют рейтинг не выше пользовательского
        if imdb_rating <= user_rating:
            imdb_ratings.append(imdb_rating)
        else:
            # Если фильм не удовлетворяет условию рейтинга, исключаем его из всех списков
            movies_id.pop()
            result_names.pop()
            result_years.pop()
            genres.pop()
            continue

    # Объединяем данные с отфильтрованными рейтингами
    combined_data = list(zip(movies_id, result_names, result_years, genres, imdb_ratings))

    # Сортируем по рейтингу IMDb в порядке убывания (от пользовательского рейтинга вниз)
    sorted_data = sorted(combined_data, key=lambda x: x[4], reverse=True)

    # Формируем итоговый список строк, не включая рейтинг IMDb в вывод
    combined_list = [f"{name} ({year}), Жанры: {', '.join(genre)}"
                     for _, name, year, genre, _ in sorted_data]

    sorted_movies_id = [movie_id for movie_id, _, _, _, _ in sorted_data]

    return combined_list, sorted_movies_id
