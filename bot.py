import telebot
from bd import test, test2
token = '6202292156:AAF0R3vpfHBL4Xviu7pxHCpCa_qWydM6jJo'
bot = telebot.TeleBot(token)
res = []
from telebot import types

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет вам подобрать задачки по теме и сложности')
    bot.send_message(message.chat.id, 'Напишите сложность: ')
    message_a = bot.send_message(message.chat.id, 'От 800 до 1500')
    bot.register_next_step_handler(message_a,
                                   save_a)

def save_a(message):
    a = int(message.text)
    message_b = bot.send_message(message.chat.id, 'Выберите категорию, для примера - "math", "greedy"')
    bot.register_next_step_handler(message_b, save_b)
    res.append(a)

def save_b(message):
    b = message.text
    res.append(b)
    print(res)

@bot.message_handler(commands=['get'])
def get(message):
    print(test(res))
    for i in test(res):
        bot.send_message(message.chat.id, str(i))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton('Новый запрос')
    btn3 = types.KeyboardButton('Подробнее о задаче')
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, 'Кнопки: ', reply_markup=markup)
    res.clear()

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Новый запрос':
        main(message)
        return res
    elif message.text == 'Подробнее о задаче':
        message_c = bot.send_message(message.chat.id, 'Введите название задачи')
        bot.register_next_step_handler(message_c,
                                       save_c)

def save_c(message):
    c = message.text
    for i in test2(c):
        bot.send_message(message.chat.id, str(i))


bot.polling(none_stop=True)