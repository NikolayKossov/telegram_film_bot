from telebot import types

def menu_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_search_film = types.KeyboardButton("🔍 Поиск по названию")
    button_search_rating_film = types.KeyboardButton("⭐ Поиск по рейтингу")
    button_history = types.KeyboardButton("📜 История пользователя")
    button_help = types.KeyboardButton("❓ Помощь")
    markup.row(button_search_film, button_search_rating_film)
    markup.row(button_history, button_help)
    return markup



