from telebot.types import Message

from api.api_search_film import search_film_at_api
from loader import bot
from database.models import User, Query, Movie
from keyboards.reply.back_button import back_to_history_button, back_to_menu_button  # Отдельные кнопки
from states.bot_stages import MyStates
from keyboards.reply import menu_buttons

@bot.message_handler(commands=["history"])
def show_history(message: Message):
    bot.set_state(message.from_user.id, MyStates.viewing_history)
    show_history_content(message)

def show_history_content(message: Message):
    username = message.from_user.username
    user, _ = User.get_or_create(username=username)

    history = Query.select().where(Query.user == user)
    saved_movies = Movie.select().where(Movie.user == user)

    response = ""

    if history.exists():
        response += "Ваша история запросов:\n"
        for record in history:
            timestamp_str = record.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            response += f"{record.movie_name} (Запрос от: {timestamp_str})\n"
    else:
        response += "Ваша история запросов пуста.\n"

    if saved_movies.exists():
        response += "\nВаши сохраненные фильмы:\n"
        for movie in saved_movies:
            response += f"{movie.title}\n"
    else:
        response += "\nУ вас нет сохраненных фильмов."

    bot.reply_to(message, response, reply_markup=back_to_menu_button())  # Только кнопка "В главное меню"
    bot.register_next_step_handler(message, handle_search_in_history)

@bot.message_handler(state=MyStates.viewing_history)
def handle_history(message: Message):
    if message.text == "🔙 Назад к истории":
        show_history_content(message)
    elif message.text == "🔝 В главное меню":
        bot.set_state(message.from_user.id, MyStates.main_menu)
        bot.send_message(
            message.chat.id,
            "Вы вернулись в главное меню.",
            reply_markup=menu_buttons.menu_buttons()
        )
    else:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, используйте кнопки для навигации.",
            reply_markup=back_to_menu_button()  # Только кнопка "В главное меню"
        )

@bot.message_handler(state=MyStates.searching_in_history)
def handle_search_in_history(message: Message):
    if message.text == "🔙 Назад к истории":
        bot.set_state(message.from_user.id, MyStates.viewing_history)
        show_history_content(message)
    elif message.text == "🔝 В главное меню":
        bot.set_state(message.from_user.id, MyStates.main_menu)
        bot.send_message(
            message.chat.id,
            "Вы вернулись в главное меню.",
            reply_markup=menu_buttons.menu_buttons()
        )
    else:
        search_in_history_content(message)

def search_in_history_content(message: Message):
    username = message.from_user.username
    user, _ = User.get_or_create(username=username)
    name = message.text
    needed_id = None
    saved_movies = Movie.select().where(Movie.user == user)

    if saved_movies.exists():
        for movie in saved_movies:
            if movie.title.lower() == name.lower():
                needed_id = str(movie.movie_id)
                break

        if needed_id:
            result, photo = search_film_at_api(needed_id)
            bot.send_photo(message.chat.id, photo, caption=result, reply_markup=back_to_history_button())  # Кнопка "Назад"
        else:
            bot.reply_to(message, "Фильм с таким названием не найден в вашей коллекции.", reply_markup=back_to_history_button())  # Кнопка "Назад"
    else:
        bot.reply_to(message, "У вас нет сохраненных фильмов для поиска.", reply_markup=back_to_history_button())  # Кнопка "Назад"

    bot.register_next_step_handler(message, handle_search_in_history)
