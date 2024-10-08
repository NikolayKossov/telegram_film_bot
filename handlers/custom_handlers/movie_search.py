from telebot.types import Message
from api import api_coonection
from database.models import User, Query
from loader import bot
from handlers.custom_handlers import choose_in_result

film_cache = {}
@bot.message_handler(commands=["movie_search"])
def movie_search(message: Message):
    bot.reply_to(message, "Введите название фильма/сериала, которого вы хотите найти")
    bot.register_next_step_handler(message, name_of_the_movie)


def name_of_the_movie(message: Message):
    username = message.from_user.username
    user, _ = User.get_or_create(username=username)
    movie_name = message.text
    Query.create(user=user, movie_name=movie_name)
    film_cache["name"] = movie_name
    bot.reply_to(message, "(Опционально) Введите жанры, которые у вашего фильма. К примеру (боевик, экшен, "
                          "приключения).")
    bot.register_next_step_handler(message, genres_of_the_movie)

def genres_of_the_movie(message: Message):
    genres = message.text
    film_cache["genres"] = genres.split()
    bot.reply_to(message, "(Опционально) Сколько фильмов выдать в поиске. По умолчанию их 10.")
    bot.register_next_step_handler(message, give_data_to_api)

def give_data_to_api(message: Message):
    pages = message.text
    film_cache["pages"] = pages
    films, movies_id = api_coonection.search_film(film_cache)
    if isinstance(films, list):
        answer = "Вот что мне удалось найти по вашему запросу:\n"
        for i, movie in enumerate(films, start=1):
            answer += f"{i}. {movie}\n"
    else:
        answer = films
    film_cache.clear()
    bot.reply_to(message, answer)
    bot.send_message(message.chat.id, "Введите цифру фильма, который вам понравился")
    bot.register_next_step_handler(message, lambda msg: choose_in_result.choose_film_from_list(msg, movies_id))





