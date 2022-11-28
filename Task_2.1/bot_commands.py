from telegram import Update
from telegram.ext import CallbackContext
import model2


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Для начала работы в калькуляторе введите /start')


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'''Для вычеслений введите через пробел\n
    "/calc число операцию число".\n
    Операции: +  *  -  /  **''')


def calc_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split() # /calc 123 + 53.4543
    if len(items) > 4:
        result = "not correct input"
    else:
        a = items[1]
        op = items[2]
        b = items[3]
        result = model2.calculation(a, op, b)
    update.message.reply_text(f'Результат = {result}')