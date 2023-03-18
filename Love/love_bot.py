import telebot
from optimize import love_func
import os

TOKEN = os.environ['6153097238:AAFM3n4GqH9Xp-1iSrruiC0Bs2uUC2dNLN0']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hello! Welcome to the Love Bot.')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    image_to_send = love_func(message.text)
    bot.send_photo(chat_id=message.chat.id, photo=image_to_send)


bot.polling(none_stop=True, interval=5)