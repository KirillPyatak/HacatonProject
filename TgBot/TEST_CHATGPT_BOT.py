import telebot
from telebot import types
import openai
import os

# Установка API-ключа OpenAI
openai.api_key = "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"

# Создание бота и подключение к Telegram API
bot = telebot.TeleBot('5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg')

# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def handle_message(message):
    # Получение запроса пользователя
    # text1 = 'Составь тестовое задание для python junior разработчика'
    # btn = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    # btn1 = (text1)
    # btn.add(btn1)
    # bot.send_message(message.chat.id,text='Нажмите кнопку, чтобы сформировать тестовое задание',reply_markup=btn)

    # user_message = message.text
    engine = "text-davinci-003"
    prompt = str(message.text)


    # Вызов API Chat GPT и получение ответа
    response =openai.Completion.create(engine=engine,
                                      prompt=prompt,
                                      temperature=0.5,
                                      max_tokens=1000)

    # Отправка ответа пользователю
    bot.send_message(message.chat.id, response.choices[0].text)

# Запуск бота
bot.polling(none_stop=True)
