import telebot
from telebot import types


bot = telebot.TeleBot('1449223275:AAGfJ8eJRGFJfAyzikq4HQ3HHNeKi9fsPTY')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item = types.KeyboardButton("Мстители:Финал")
    markup.add(item)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nЧтобы узнать данные о фильме Мстители:Финал напиши мне\n" 
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    if message.chat.type == 'private':
        if message.text == 'Мстители' or 'Мстители:Финал' or 'Мстители Финал' or 'мстители финал' or 'мстители':
            img = open("static/avenger123.jpg", "rb")
            bot.send_photo(message.chat.id, img)
            final_message = f"Мстители: Финал\n\nОставшиеся в живых члены команды Мстителей и их союзники должны разработать новый план, который поможет противостоять разрушительным действиям могущественного титана Таноса. После наиболее масштабной и трагической битвы в истории они не могут допустить ошибку."
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить...')


# Это нужно чтобы бот работал
bot.polling(none_stop=True)