import telebot

BOT_TOKEN = 8844663921:AAE8xpgYFxXwS3XgNu6IfYXe4Y0XqSiohr0

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello 👋 Bilal Bot working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.infinity_polling()