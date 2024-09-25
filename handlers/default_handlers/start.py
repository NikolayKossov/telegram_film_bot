from telebot.types import Message
from loader import bot
from database.models import User
from keyboards.reply import menu_buttons
import handlers
from states.bot_stages import MyStates


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    username = message.from_user.username
    user, created = User.get_or_create(username=username)
    bot.set_state(message.from_user.id, MyStates.main_menu)

    if created:
        bot.reply_to(
            message,
            f"Привет, {message.from_user.full_name}! Я бот для поиска фильмов.",
            reply_markup=menu_buttons.menu_buttons()  # Отправляем клавиатуру меню
        )
    else:
        bot.reply_to(
            message,
            f"О, это снова вы, {message.from_user.full_name}. Рад вас видеть!",
            reply_markup=menu_buttons.menu_buttons()  # Отправляем клавиатуру меню
        )


@bot.message_handler(func=lambda message: True)
def handle_button_click(message: Message):
    if message.text == "🔍 Поиск по названию":
        handlers.custom_handlers.movie_search.movie_search(message)
    elif message.text == "⭐ Поиск по рейтингу":
        handlers.custom_handlers.movie_by_rating.rating_movie_search(message)
    elif message.text == "📉 Поиск с низким бюджетом":
        handlers.custom_handlers.movie_by_low_budget.budget_movie_search(message)
    elif message.text == "📈 Поиск с высоким бюджетом":
        handlers.custom_handlers.movie_by_high_budget.budget_movie_search(message)
    elif message.text == "📜 История пользователя":
        handlers.custom_handlers.history.show_history(message)
    elif message.text == "❓ Помощь":
        handlers.default_handlers.help.bot_help(message)



