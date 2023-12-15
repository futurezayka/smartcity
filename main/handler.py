from telebot import TeleBot as Handler
from smartcity.settings import BOT_TOKEN


def handle_form(data):
    message = f'Новая заявка на резюме\n' \
              f'Имя: {data["name"]}\n' \
              f'Телефон: {data["phone"]}\n' \
              f'Почта: {data["email"]}\n' \
              f'Сообщение: {data["message"]}'
    bot = Handler(BOT_TOKEN)
    chat_id = '-4047928606'
    bot.send_message(chat_id=chat_id, text=message)
