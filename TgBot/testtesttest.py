import telebot
import sqlite3

# Инициализация бота
bot = telebot.TeleBot("5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg")

# Инициализация базы данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы с информацией о кандидатах
cursor.execute('CREATE TABLE IF NOT EXISTS candidates (id INTEGER PRIMARY KEY, name TEXT, experience TEXT, contacts TEXT)')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для автоматизации подбора персонала. Введите /add_candidate чтобы добавить кандидата или /get_candidates чтобы получить список кандидатов.")

# Обработчик команды /add_candidate
@bot.message_handler(commands=['add_candidate'])
def add_candidate(message):
    bot.reply_to(message, "Введите имя кандидата:")
    bot.register_next_step_handler(message, add_candidate_experience)

def add_candidate_experience(message):
    name = message.text
    bot.reply_to(message, "Введите опыт работы кандидата:")
    bot.register_next_step_handler(message, add_candidate_contacts, name)

def add_candidate_contacts(message, name, experience):
    experience = message.text
    bot.reply_to(message, "Введите контакты кандидата:")
    bot.register_next_step_handler(message, save_candidate, name, experience)

def save_candidate(message, name, experience):
    contacts = message.text
    cursor.execute("INSERT INTO candidates (name, experience, contacts) VALUES (?, ?, ?)", (name, experience, contacts))
    conn.commit()
    bot.reply_to(message, "Кандидат успешно добавлен в базу данных!")

# Обработчик команды /get_candidates
@bot.message_handler(commands=['get_candidates'])
def get_candidates(message):
    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()
    response = "Список кандидатов:\n"
    for candidate in candidates:
        response += f"ID: {candidate[0]}, Имя: {candidate[1]}, Опыт: {candidate[2]}, Контакты: {candidate[3]}\n"
    bot.reply_to(message, response)

# Запуск бота
bot.polling()