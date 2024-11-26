import telebot

bot = telebot.TeleBot('7705738513:AAFwg3uHSQejg3u0s_CIiwDKwsFvYHnPfZQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Привет!Давай потренируемся?*', parse_mode='Markdown')

@bot.message_handler(commands=['addition'])
def main_1(message):
    bot.send_message(message.chat.id, '*Сколько будет 5+6?*', parse_mode='Markdown')

@bot.message_handler(commands=['subtraction'])
def main_2(message):
    bot.send_message(message.chat.id, '*Сколько будет 27-13?*', parse_mode='Markdown')

@bot.message_handler(commands=['multiplication'])
def main_3(message):
    bot.send_message(message.chat.id, '<b>Сколько будет 50*3?</b>', parse_mode='HTML')

@bot.message_handler(commands=['end'])
def main_4(message):
    bot.send_message(message.chat.id, '*Ты хорошо поработал.Молодец!*', parse_mode='Markdown')


bot.infinity_polling()


