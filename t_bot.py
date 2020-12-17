#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
from telebot import types


bot = telebot.TeleBot('1450748089:AAHq2ovog23hW7TEpWIrx4eEiNtr8Uewd3o')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Мстители:Финал")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item2 = types.KeyboardButton("Мстители")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item3 = types.KeyboardButton("Мстители: Эра Альтрона")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item4 = types.KeyboardButton("Мстители:Война бесконечности")
    markup.add(item1, item2, item3, item4)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nЧтобы узнать данные о фильме Мстители:Финал напиши мне\n" 
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    if message.chat.type == 'private':
        if message.text == 'Мстители:Финал':
            img = open("static/avenger123.jpg", "rb")
            bot.send_photo(message.chat.id, img)
            final_message = f"Мстители: Финал\n\nОставшиеся в живых члены команды Мстителей и их союзники должны разработать новый план, который поможет противостоять разрушительным действиям могущественного титана Таноса. После наиболее масштабной и трагической битвы в истории они не могут допустить ошибку."
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Мстители':
            img = open("static/avenger.jpg", "rb")
            bot.send_photo(message.chat.id, img)
            final_message = f"Мстители\n\nЗамысел преступника - покорить мир, ввергнув его в холод и стужу... Фантастические трюки, масштабные декорации, эффектные костюмы Эммы, - все это в сочных красках, под музыку Шиннед О`Коннор и Энни Леннокс."
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Мстители: Эра Альтрона':
            img = open("static/ave.jpg", "rb")
            bot.send_photo(message.chat.id, img)
            final_message = f"Мстители: Эра Альтрона\n\nЧеловечество на грани уничтожения. На этот раз людям угрожает Альтрон — искусственный интеллект, ранее созданный для того, чтобы защищать Землю от любых угроз. Однако, главной угрозой он посчитал человечество. Международная организация Щ.И.Т. распалась, и теперь мир не способен справиться с таким мощным врагом, потому люди вновь обращаются за помощью к Величайшим Героям Земли — Мстителям. Однако Альтрон слишком силен, и есть большая вероятность, что даже им не удастся остановить начало надвигающейся Эры Альтрона, где нет места для людей…"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Мстители:Война бесконечности':
            img = open("static/av.jpg", "rb")
            bot.send_photo(message.chat.id, img)
            final_message = f"Мстители: Война бесконечности\n\nПока Мстители и их союзники продолжают защищать мир от различных опасностей, с которыми не смог бы справиться один супергерой, новая угроза возникает из космоса: Танос. Межгалактический тиран преследует цель собрать все шесть Камней Бесконечности - артефакты невероятной силы, с помощью которых можно менять реальность по своему желанию. Всё, с чем Мстители сталкивались ранее, вело к этому моменту – судьба Земли никогда ещё не была столь неопределённой."
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить...')


# Это нужно чтобы бот работал
bot.polling(none_stop=True)