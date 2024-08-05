from telebot.types import Message
from loader import bot
from database import sqlite
from database.models import Request


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}! Я бот для поиска фильмов.")
    sqlite.db.connect()
    sqlite.db.create_tables([Request])  
    sqlite.db.close()


