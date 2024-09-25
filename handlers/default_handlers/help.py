from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS, CUSTOM_COMMANDS
from loader import bot

@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text1 = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    text2 = [f"/{command} - {desk}" for command, desk in CUSTOM_COMMANDS]
    combined_text = text1 + text2
    bot.reply_to(message, "\n".join(combined_text))



