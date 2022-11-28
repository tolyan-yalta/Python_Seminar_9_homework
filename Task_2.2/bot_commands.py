from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext
import time


load_file = None
type_file = None
last_file_name = None

data = None
new_data = []
data_changed = None
massage = None
find_element = []


def select_file_format(format_file):
    # нажатие кнопки "Выберите формат файла"
    global load_file
    global type_file
    global last_file_name

    match format_file:
        case '1':
            load_file = True
            type_file = 'xml'
            last_file_name = 'data.xml'
        case '4':
            load_file = True
            type_file = 'csv'
            last_file_name = 'data.csv'
        case _:
            type_file = None


def transfer_load_file():
    # Перенос из bot данных для загрузки из файла
    global load_file
    global type_file
    global last_file_name
    return load_file, type_file, last_file_name


def transfer_load_file_reset():
    # Сброс информации о загрузке из файла
    global load_file
    load_file = None       


def transfer_data(tr_data):
    # Перенос данных в bot
    global data
    data = tr_data


def transfer_data_from_bot():
    # Перенос данных из bot
    global data
    return data


def transfer_add_data():
    # Перенос из бота информации о добавлении данных
    global data_changed
    return data_changed


def transfer_add_data_reset():
    # Сброс информации о добавлении данных
    global data_changed
    data_changed = None


def find_new_id():
        # Находится последний id  и создается новый
        global data
        temp = [int(i[0]) for i in data]
        temp.sort()
        return str(temp[-1] + 1)


def get_new_data():
        # Добавляются новые данные и устанавливается флаг наличия новых данных
        global data
        global data_changed
        global new_data
        data = data + new_data
        data_changed = True


def listing(update: Update, context: CallbackContext):
    global data
    persons = [list(i) for i in data]
    rows = [' '.join(i) for i in persons]
    [update.message.reply_text(f'{i}') for i in rows]


def search(update: Update, context: CallbackContext):
    global massage
    global data
    global find_element
    if massage != '':
        find_element = []
        for elem in data:
            for subelem in elem:
                if subelem == (None or ""):
                    break
                if massage in subelem:
                    find_element.append(elem)
                    break
    if len(find_element) == 0:
        find_element = ['Ничего не найдено']
    t = [list(i) for i in find_element]
    p = [' '.join(i) for i in t]
    [update.message.reply_text(f'{i}') for i in p]


def add_data(update: Update, context: CallbackContext):
    # Получаем данные из сообщения
    global massage
    massage = update.message.text


# Этапы/состояния разговора
FIRST, SECOND = range(2)
# Данные обратного вызова
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGTH, NINE, TEN, ELEVEN, TWELVE = range(12)

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/help\n/start')


def start(update: Update, context: CallbackContext):
    # Вызывается по команде `/start`
    keyboard = [[InlineKeyboardButton("Давай заглянем", callback_data=str(NINE)),
            InlineKeyboardButton("Нет", callback_data=str(TEN)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text="Привет, хочешь заглянуть в телефонный справочник?", reply_markup=reply_markup)
    return SECOND


def start_over(update: Update, context: CallbackContext):
    # Возвращение к началу диалога
    query = update.callback_query
    query.answer()
    keyboard = [[InlineKeyboardButton("Да", callback_data=str(ONE)),
            InlineKeyboardButton("Нет", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Загрузить телефонный справочник?", reply_markup=reply_markup)
    return FIRST


def one(update: Update, context: CallbackContext):
    # Выбор формата файла
    global type_file
    query = update.callback_query
    query.answer()
    keyboard = [[InlineKeyboardButton("В формате XML", callback_data=str(TWO)), 
                InlineKeyboardButton("В формате CSV", callback_data=str(FIVE)), 
                InlineKeyboardButton("Закрыть", callback_data=str(EIGTH))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Выберите формат файла:", reply_markup=reply_markup)
    return FIRST


def two(update: Update, context: CallbackContext):
    # Получаем ответ при выборе xml
    query = update.callback_query
    query.answer()
    # Присваиваем переменной полученный ответ и передаем его для загрузки данных
    format_file = query.data
    # print(format_file)
    select_file_format(format_file)
    # Задержка чтобы controller успел загрузить данные
    time.sleep(0.05)
    keyboard = [[InlineKeyboardButton("Добавить", callback_data=str(THREE)), 
            InlineKeyboardButton("Поиск", callback_data=str(ELEVEN)), 
            InlineKeyboardButton("Закрыть", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Для просмотра справочника\nнажмите или введите - /listing", reply_markup=reply_markup)
    return FIRST


def three(update: Update, context: CallbackContext):
    # Получаем ответ при выборе "Добавить данные"
    query = update.callback_query
    query.answer()
    btn_save_xml = query.data
    # print(btn_save_xml)
    keyboard = [[InlineKeyboardButton("Сохранить", callback_data=str(FOUR)),
            InlineKeyboardButton("Нет", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text='''Введите данные через пробел\n 
    "Фамилия Имя Отчество Телефон E-mail"\n
     после нажмите кнопку "Сохранить"''', reply_markup=reply_markup)
    return FIRST


def four(update: Update, context: CallbackContext):
    
    query = update.callback_query
    query.answer()
    btn_save_xml = query.data
    if btn_save_xml == '3':
        if massage != '':
            new_person = massage.split()
            if len(new_person) < 5:
                temp = 5 - len(new_person)
                for _ in range(temp):
                    new_person.append('')
            new_data = [(find_new_id(), new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])]
        get_new_data()
    keyboard = [[InlineKeyboardButton("Продолжить", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Данные сохранены", reply_markup=reply_markup)
    return FIRST


def five(update: Update, context: CallbackContext):
    # Получаем ответ при выборе csv
    query = update.callback_query
    query.answer()
    # Присваиваем переменной полученный ответ и передаем его для загрузки данных
    format_file = query.data
    select_file_format(format_file)
    # print(format_file)
    # Задержка чтобы controller успел загрузить данные
    time.sleep(0.05)
    keyboard = [[InlineKeyboardButton("Добавить", callback_data=str(SIX)), 
            InlineKeyboardButton("Найти", callback_data=str(ELEVEN)), 
            InlineKeyboardButton("Закрыть", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Для просмотра справочника\nнажмите или введите - /listing", reply_markup=reply_markup)
    return FIRST


def six(update: Update, context: CallbackContext):
    # Получаем ответ при выборе "Добавить данные"
    query = update.callback_query
    query.answer()
    btn_save_csv = query.data
    # print(btn_save_csv)
    keyboard = [[InlineKeyboardButton("Сохранить", callback_data=str(SEVEN)),
            InlineKeyboardButton("Нет", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text='''Введите данные через пробел\n 
    "Фамилия Имя Отчество Телефон E-mail"\n
     после нажмите кнопку "Сохранить"''', reply_markup=reply_markup)
    return FIRST


def seven(update: Update, context: CallbackContext):
    global massage
    global new_data
    query = update.callback_query
    query.answer()
    btn_save_csv = query.data
    if btn_save_csv == '6':
        if massage != '':
            new_person = massage.split()
            if len(new_person) < 5:
                temp = 5 - len(new_person)
                for _ in range(temp):
                    new_person.append('')
            new_data = [(find_new_id(), new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])]
        get_new_data()
    keyboard = [[InlineKeyboardButton("Продолжить", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Данные сохранены", reply_markup=reply_markup)
    return FIRST


def eigth(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    btn_no = query.data
    # print(btn_no)
    keyboard = [[InlineKeyboardButton("Загрузить снова", callback_data=str(NINE)),
            InlineKeyboardButton("Выйти из справочника", callback_data=str(TEN)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Закрыть справочник", reply_markup=reply_markup)
    return SECOND


def eleven(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [[InlineKeyboardButton("Закрыть", callback_data=str(EIGTH)),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text='Введите информацию для поиска\nНайти - /search', reply_markup=reply_markup)
    return FIRST


def end(update: Update, context: CallbackContext):
    # Завершение диалога
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Спасибо, до свидания!")
    return ConversationHandler.END

