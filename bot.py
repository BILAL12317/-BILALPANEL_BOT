import os
import telebot

BOT_TOKEN = os.getenv("8844663921:AAE8xpgYFxXwS3XgNu6IfYXe4Y0XqSiohr0")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bilal bot working ✅")

bot.infinity_polling()