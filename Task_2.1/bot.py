# from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *


with open('F:/Учеба в ГикБрэйнс/21. Знакомство с языком Python/telegram_bot_token.txt', 'r') as f:
    token = str(f.read())
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('calc', calc_command))
print('server start')
updater.start_polling()
updater.idle()