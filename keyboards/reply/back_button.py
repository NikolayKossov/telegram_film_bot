from telebot import types

def back_to_history_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_back_to_history = types.KeyboardButton("🔙 Назад к истории")
    markup.row(button_back_to_history)
    return markup

def back_to_menu_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_back_to_menu = types.KeyboardButton("🔝 В главное меню")
    markup.row(button_back_to_menu)
    return markup
