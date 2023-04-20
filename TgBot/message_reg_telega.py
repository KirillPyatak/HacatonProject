from telebot import types
import telebot

izmenitbuttons = types.InlineKeyboardMarkup(row_width=2)
name_izmenit = types.InlineKeyboardButton('Имя', callback_data='name_izmenit')
mail_izmenit = types.InlineKeyboardButton('Mail', callback_data='mail_izmenit')
city_izmenit = types.InlineKeyboardButton('Город', callback_data='city_izmenit')
age_izmenit = types.InlineKeyboardButton('Возраст', callback_data='age_izmenit')
podtverdit = types.InlineKeyboardButton('✅Подтвердить данные', callback_data='podtverdit')
izmenitbuttons.add(name_izmenit, mail_izmenit, city_izmenit, age_izmenit)
izmenitbuttons.add(podtverdit)


keyboard_edit = types.InlineKeyboardMarkup()
edit_button = types.InlineKeyboardButton("Сформировать тз", callback_data='edit_button')
keyboard_edit.add(edit_button)

keyboard_edit2 = types.InlineKeyboardMarkup()
edit_button2 = types.InlineKeyboardButton("Сформировать задание", callback_data='edit_button2')
keyboard_edit2.add(edit_button2)