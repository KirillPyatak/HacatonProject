import telebot
from telebot import types
from flask import Flask, render_template, request
import requests
from flask_ngrok import run_with_ngrok
#rest api для связи flask react

app = Flask(__name__)


# 6225681760:AAEpcmqK-IQJbxeV-VAxHbtOnTHw41D-oeg новый бот
# 5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg старый бот
# мой айдишник 406299011
# айдишник чата -1001923842541

TOKEN = '6225681760:AAEpcmqK-IQJbxeV-VAxHbtOnTHw41D-oeg'
CHAT_ID = '406299011'

bot = telebot.TeleBot(TOKEN)


# @app.route("/setwebhook/")
# def setwebhook():
#     url = "https://your-ngrok-URL.ngrok.io/"
#     s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(TOKEN, url))
#
#     if s:
#         return "Success"
#     else:
#         return "fail"

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     message_name = request.form['name_message']
    #     message_email = request.form['email_message']
    #     message_city = request.form['city_message']
    #     message_file = request.files['file_message']
    #
    #     response = (message_name)
    #     response = (message_email)
    #     response = (message_city)
    #     # response = send_message_to_bot(message_email)
    #     izmenitbuttons = types.InlineKeyboardMarkup(row_width=2)
    #     name_izmenit = types.InlineKeyboardButton('Имя', callback_data='name_izmenit')
    #     mail_izmenit = types.InlineKeyboardButton('Mail', callback_data='mail_izmenit')
    #     city_izmenit = types.InlineKeyboardButton('Город', callback_data='city_izmenit')
    #     age_izmenit = types.InlineKeyboardButton('Возраст', callback_data='age_izmenit')
    #     podtverdit = types.InlineKeyboardButton('✅Подтвердить данные', callback_data='podtverdit')
    #     izmenitbuttons.add(name_izmenit, mail_izmenit, city_izmenit, age_izmenit)
    #     izmenitbuttons.add(podtverdit)
    #     bot.send_document(CHAT_ID, caption="Имя: "+message_name+"\nmail: "+message_email+'\nГород:'+message_city, document=message_file, reply_markup=izmenitbuttons)

    return render_template('index.html')


# def send_message_to_bot(message):
#     response = bot.send_message(CHAT_ID, message)
    # здесь мы используем библиотеку pyTelegramBotAPI, чтобы отправить сообщение в телеграм



# def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
#     startbutton = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     openweb = types.WebAppInfo('http://0520-178-66-158-205.ngrok-free.app')
#     startbutton1 = types.KeyboardButton(text='открыть веб страницу', web_app=openweb)
#     startbutton.add(startbutton1)
#     return startbutton #возвращаем клаву

#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=webAppKeyboard())

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я чат-менеджер на сайте. Как я могу тебе помочь?")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)



run_with_ngrok(app)
if __name__ == '__main__':
    app.run()

