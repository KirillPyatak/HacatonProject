import json
from message_reg_telega import *
from telebot import types
import telebot
from main import index
import requests
import sqlite3
import openai

TOKEN = '5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg'
CHAT_ID = '-1001923842541'
openai.api_key = "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"
bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS candidates (id INTEGER PRIMARY KEY, name TEXT, email TEXT, city TEXT)')


@bot.message_handler(commands=['start'])
def start(message):
    # Получите ID пользователя
    user_id = message.from_user.id
    # print(user_id)
    message_user = message.message_id
    # print(message_user)

    # Проверьте, подписался ли пользователь на ваш канал
    subscribed = bot.get_chat_member(CHAT_ID, user_id).status in ['member', 'administrator', 'creator']
    startbutton = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if not subscribed:
        openweb = types.WebAppInfo('https://25f4-92-255-89-234.ngrok-free.app')
        startbutton1 = types.KeyboardButton(text='открыть веб страницу', web_app=openweb)
        startbutton.add(startbutton1)
        bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=startbutton)
    else:
        bot.send_message(message.chat.id, 'Здравствуй, дорогой HR',reply_markup=keyboard_edit2)

@bot.message_handler(content_types=['web_app_data'])
def web_app(webAppMes):
    print(webAppMes)
    print(webAppMes.web_app_data.data)
    res = json.loads(webAppMes.web_app_data.data)
    a = str(res["name"])
    b = str(res["email"])
    c = str(res["city"])

    bot.send_message(CHAT_ID, text=(f'Имя: '+ a +'\nMail: '+b + '\nГород: ' + c),
                     reply_markup=keyboard_edit)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    from_chat_id = call.message.chat.id
    if call.data == 'edit_button2':
        engine = "text-davinci-003"
        prompt = str('создай тестовое задание высокой сложности для python разработчика')

        # Вызов API Chat GPT и получение ответа
        response = openai.Completion.create(engine=engine,
                                            prompt=prompt,
                                            temperature=0.5,
                                            max_tokens=1000)

        # Отправка ответа пользователю
        bot.edit_message_text(chat_id=call.message.chat.id, text=response.choices[0].text, message_id=call.message.message_id,)







# def save_candidat(call):
#     global res
#
#     if call.data == 'podtverdit':
#         cursor.execute("INSERT INTO candidates (name, email, city) VALUES (?, ?, ?)", ({res['name']}, {res['email']}, {res['city']}) )
#         conn.commit()
#         bot.send_message(call.messaage.chat.id, "Кандидат успешно добавлен в базу данных!")


# name = ''
# mail = ''
# city = ''
# age = 0
#
#
# izmenitbuttons = types.InlineKeyboardMarkup(row_width=2)
# name_izmenit = types.InlineKeyboardButton('Имя', callback_data='name_izmenit')
# mail_izmenit = types.InlineKeyboardButton('Mail', callback_data='mail_izmenit')
# city_izmenit = types.InlineKeyboardButton('Город', callback_data='city_izmenit')
# age_izmenit = types.InlineKeyboardButton('Возраст', callback_data='age_izmenit')
# izmenitbuttons.add(name_izmenit,mail_izmenit,city_izmenit,age_izmenit)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     startbutton = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     name = types.KeyboardButton("отправить имя")
#     startbutton.add(name)
#     bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)',reply_markup=startbutton)
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#       bot.send_message(message.from_user.id, "Напиши имя и фаимилю")
#       bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
#     # else:
#     #   bot.send_message(message.from_user.id, 'Напиши /reg')
#
#
# def get_name(message):  # получаем имя
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Напиши адрес эл. почты:')
#     bot.register_next_step_handler(message, get_mail)  # следующий шаг – функция get_surname
#
#
# def get_mail(message):  # получаем фамилию
#     global mail
#     mail = message.text
#     bot.send_message(message.from_user.id, 'Из какого ты города?')
#     bot.register_next_step_handler(message, get_city)
#
# def get_city(message):  # получаем город
#     global city
#
#     city = message.text
#     bot.send_message(message.from_user.id,'Введите ваш возраст:')
#     bot.register_next_step_handler(message, get_age)
# def get_age(message):  # получаем возраст
#     global age
#         # проверяем, что возраст введен корректно
#     age = message.text
#     a = bot.send_message(message.chat.id,
#                          "Имя: " + name + "\nmail: " + mail + "\nГород: " + city + "\nВозраст: " + age,
#                          reply_markup=izmenitbuttons)
#     bot.register_next_step_handler(message, izmenit)
#
# def izmenit(message):
#     bot.send_message(message.chat.id,
#                      "Имя: " + name + "\nmail: " + mail + "\nГород: " + city + "\nВозраст: " + age,
#                      reply_markup=izmenitbuttons)
#
#


# Запуск бота
bot.polling(none_stop=True)
