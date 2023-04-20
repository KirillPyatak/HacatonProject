import telebot
from telebot import types
import sqlite3
from flask import Flask, render_template, request
import json
from message_reg_telega import *
import requests
from flask_ngrok import run_with_ngrok
#rest api для связи flask react

app = Flask(__name__)


TOKEN = '6225681760:AAEpcmqK-IQJbxeV-VAxHbtOnTHw41D-oeg'
CHAT_ID = '406299011'

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS candidates (id INTEGER PRIMARY KEY, name TEXT, email TEXT, city TEXT)')


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

@bot.message_handler(commands=['start'])
def start(message):
    startbutton = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    openweb = types.WebAppInfo('https://2edf-178-66-158-205.ngrok-free.app')
    startbutton1 = types.KeyboardButton(text='открыть веб страницу', web_app=openweb)
    startbutton.add(startbutton1)
    bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=startbutton)

@bot.message_handler(content_types='web_app_data')
def web_app(webAppMes):
    print(webAppMes)
    print(webAppMes.web_app_data.data)
    res = json.loads(webAppMes.web_app_data.data)
    bot.send_message(CHAT_ID, text = f'Имя: {res["name"]} \nMail: {res["email"]} \nГород: {res["city"]}',
                     reply_markup=izmenitbuttons)
def save_candidat(call,res):
    if call.data == 'podtverdit':
        cursor.execute("INSERT INTO candidates (name, email, city) VALUES (?, ?, ?)", ({res['name']}, {res['email']}, {res['city']}) )
        conn.commit()
        bot.send_message(call.messaage.chat.id, "Кандидат успешно добавлен в базу данных!")



#
run_with_ngrok(app)
if __name__ == '__main__':
    bot.polling();
    app.run();

