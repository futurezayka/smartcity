from telebot import TeleBot as Handler
from smartcity.settings import BOT_TOKEN


def handle_form(data):
    message = f'Новое резюме:\n' \
              f'Имя: {data["name"]}\n' \
              f'Фамилия: {data["surname"]}\n' \
              f'Почта: {data["email"]}\n' \
              f'Специализация: {data["spec"]}'
    bot = Handler(BOT_TOKEN)
    chat_id = '-4047928606'
    bot.send_message(chat_id=chat_id, text=message)
