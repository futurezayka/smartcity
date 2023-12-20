from telebot import TeleBot as Handler

from main.models import Vacancy
from smartcity.settings import BOT_TOKEN


def handle_resume(data):
    message = f'<b>Отримано нове резюме</b>\n' \
              f'Ім\'я: {data["name"]}\n' \
              f'Прізвище: {data["surname"]}\n' \
              f'Електронна пошта: {data["email"]}\n' \
              f'Спеціалізація: {data["spec"]}'
    return send_message(message)


def handle_application(data):
    vacancy = Vacancy.objects.filter(id=data['vacancy_pk']).first()
    message = f'<b>Отримано нову заявку</b>\n' \
              f'Ім\'я: {data["name"]}\n' \
              f'Прізвище: {data["surname"]}\n' \
              f'Номер телефону: {data["phone"]}\n' \
              f'Вакансія: {vacancy.title}\n'
    return send_message(message)


def send_message(message):
    bot = Handler(BOT_TOKEN)
    chat_id = '-4047928606'
    bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
