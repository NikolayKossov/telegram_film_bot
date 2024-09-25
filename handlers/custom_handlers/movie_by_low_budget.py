from telebot.types import Message
from loader import bot
from api import api_low_budget_movie
from handlers.custom_handlers.choose_in_result import choose_film_from_list


@bot.message_handler(commands=["low_budget_movie"])
def budget_movie_search(message: Message):
    bot.reply_to(message, "Вот фильмы с самым низким бюджетом")
    movie_search_result_low(message)

def movie_search_result_low(message: Message):
    films, movies_id = api_low_budget_movie.search_film_at_api_low_budget()
    if isinstance(films, list):
        answer = "Вот что мне удалось найти по вашему запросу:\n"
        for i, movie in enumerate(films, start=1):
            answer += f"{i}. {movie}\n"
    else:
        answer = films
    bot.reply_to(message, answer)
    bot.send_message(message.chat.id, "Введите цифру фильма, который вам понравился")
    bot.register_next_step_handler(message, lambda msg: choose_film_from_list(msg, movies_id))

def test(message: Message):
    bot.reply_to(message, "Тест сообщение")
