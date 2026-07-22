import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")  

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bilal bot working ✅")

bot.infinity_polling()