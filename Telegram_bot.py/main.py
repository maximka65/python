import telebot

bot = telebot.TeleBot("889305522:AAHE1_V8JC7Upg4VCHbsKLDeDIalq8X8zOQ")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Whatsup")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message, message.text)


bot.polling(True)
