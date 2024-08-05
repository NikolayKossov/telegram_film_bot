from telebot.types import Message
from loader import bot
from api.api_coonection import search_film


@bot.message_handler(commands=["movie_search"])
def movie_search(message: Message):
    bot.reply_to(message, "Введите фильм, который хотите найти")
    bot.register_next_step_handler(message, movie_search_result)

def movie_search_result(message: Message):
    movie_name = message.text
    films = search_film(movie_name)
    if isinstance(films, list):
        answer = "Вот что мне удалось найти по вашему запросу:\n"
        for i, movie in enumerate(films, start=1):
            answer += f"{i}. {movie}\n"
    else:
        answer = films
    bot.reply_to(message, answer)
    bot.send_message(message.chat.id, "Введите цифру фильма, который вам понравился")



