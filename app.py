from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
# Для отрисовки в боте клавиатуры
from telegram import ReplyKeyboardMarkup
# Для обращеиня к внешнему api
import requests  
# Для работы с .env файлом
from dotenv import load_dotenv

import os

# загружаем переменные окружения из .env файла
load_dotenv()


BOT_TOKEN = os.getenv('bot_token')

URL = 'https://api.thecatapi.com/v1/images/search'

# Объект для обработки и получения входящих сообщений
updater = Updater(token=BOT_TOKEN)


def get_image():
    """Возвращает url случайной картинки для последующей отправки ботом"""
    response = requests.get(URL).json()
    image_url = response[0].get('url')
    return image_url


def wake_up(update, context):
    """Отправляет приветствие с именем пользователя"""
    chat = update.effective_chat
    # Пример работы с объектом message. Достаем имя контакта
    name = update.message.chat.first_name
    message = f'{name}, спасибо что присоединились!'
    # Создаем кнопку вызова команды, для отправки в ответе
    button = ReplyKeyboardMarkup([['/new_image']])
    context.bot.send_message(chat_id=chat.id, text=message, reply_markup=button)


def new_image(update, context):
    """Отправляет картинку"""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_image())


def reverse_text(update, context):
    """Отправляет первернутый текст полученного сообщения"""
    chat = update.effective_chat
    message = update.message.text[::-1]
    context.bot.send_message(chat_id=chat.id, text=message)


# Этот обработчик срабатывает на команду /start ,
# перенаправляя вызов в функцию wake_up
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
# Этот обработчик срабатывает на команду /new_image
updater.dispatcher.add_handler(CommandHandler('new_image', new_image))
# Обрабатываем все остальные текстовые сообщения
updater.dispatcher.add_handler(MessageHandler(Filters.text, reverse_text))


# Метод start_polling() запускает процесс опроса обновлений
# приложение начнёт отправлять регулярные запросы каждые 10 сек
updater.start_polling(poll_interval=10.0)
# Бот будет работать до тех пор, пока не будет прервано выполнения скрипта через ctrl+c
updater.idle()
