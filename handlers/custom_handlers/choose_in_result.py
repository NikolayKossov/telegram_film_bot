from api.api_search_film import search_film_at_api
from loader import bot
from telebot.types import Message
from database.models import User, Movie


def choose_film_from_list(message: Message, ideas):
    index_from_list = int(message.text)
    indexes = len(ideas)
    need_film_id = None

    for index in range(indexes):
        if index == index_from_list:
            need_film_id = index
            break

    # Получаем ID фильма
    film_id = ideas[need_film_id - 1]

    # Получаем результат и фото фильма
    result, photo = search_film_at_api(film_id)

    # Отправляем фото и описание фильма пользователю
    bot.send_photo(message.chat.id, photo, caption=result)

    # Получаем имя пользователя и создаем/получаем объект User
    username = message.from_user.username
    user, _ = User.get_or_create(username=username)

    # Извлекаем название фильма из `result`
    title = result.split("\n")[0]  # Предполагаем, что название фильма идет первой строкой

    movie_exists = Movie.select().where(Movie.user == user, Movie.movie_id == film_id).exists()

    if not movie_exists:
        Movie.create(user=user, title=title, movie_id=film_id)