# Создайте программу для игры в ""Крестики-нолики"".

def victory(f):
    # Проверка на завершение игры по победе одной из сторон
    # В случае если три ячейки в линию принадлежат одной из сторон, то возвращается True и содержимое одной из ячеек
    # (ячейка может быть любой из трех). Содержимое (1 или 2) указывает кто победил.
    # Иначе возвращается False и None.
    if f[0] == f[1] == f[2] == 1 or f[0] == f[1] == f[2] == 2:
        return True, f[0]
    elif f[3] == f[4] == f[5] == 1 or f[3] == f[4] == f[5] == 2:
        return True, f[3]
    elif f[6] == f[7] == f[8] == 1 or f[6] == f[7] == f[8] == 2:
        return True, f[6]
    elif f[0] == f[3] == f[6] == 1 or f[0] == f[3] == f[6] == 2:
        return True, f[0]
    elif f[1] == f[4] == f[7] == 1 or f[1] == f[4] == f[7] == 2:
        return True, f[1]
    elif f[2] == f[5] == f[8] == 1 or f[2] == f[5] == f[8] == 2:
        return True, f[2]
    elif f[0] == f[4] == f[8] == 1 or f[0] == f[4] == f[8] == 2:
        return True, f[0]
    elif f[2] == f[4] == f[6] == 1 or f[2] == f[4] == f[6] == 2:
        return True, f[2]
    else:
        return False, None

def logic_attack(value):
    # Логика для завершения игры победой.
    # Если две клетки в линию заняты ботом а третья пустая, то возвращается индекс клетки которую необходимо занять чтобы победить.
    # Если нет такой возможности, то возвращается 9 (такой клетки нет)
    if value[0] == 2 and value[1] == 2 and value[2] == 0:    # ветка 0
        return 2
    elif value[2] == 2 and value[5] == 2 and value[8] == 0:
        return 8
    elif value[8] == 2 and value[7] == 2 and value[6] == 0:
        return 6
    elif value[6] == 2 and value[3] == 2 and value[0] == 0:
        return 0

    if value[1] == 2 and value[2] == 2 and value[0] == 0:  # ветка 1
        return 0
    elif value[5] == 2 and value[8] == 2 and value[2] == 0:
        return 2
    elif value[7] == 2 and value[6] == 2 and value[8] == 0:
        return 8
    elif value[3] == 2 and value[0] == 2 and value[6] == 0:
        return 6

    if value[0] == 2 and value[2] == 2 and value[1] == 0:  # ветка 2
        return 1
    elif value[2] == 2 and value[8] == 2 and value[5] == 0:
        return 5
    elif value[8] == 2 and value[6] == 2 and value[7] == 0:
        return 7
    elif value[6] == 2 and value[0] == 2 and value[3] == 0:
        return 3

    if value[4] == 2 and value[1] == 2 and value[7] == 0:    # ветка 3
        return 7
    elif value[4] == 2 and value[5] == 2 and value[3] == 0:
        return 3
    elif value[4] == 2 and value[7] == 2 and value[1] == 0:
        return 1
    elif value[4] == 2 and value[3] == 2 and value[5] == 0:
        return 5

    if value[1] == 2 and value[7] ==2 and value[4] == 0:  # ветка 4
        return 4
    elif value[3] == 2 and value[5] == 2 and value[4] == 0:
        return 4

    if value[4] == 2 and value[2] == 2 and value[6] == 0:  # ветка 5
        return 6
    elif value[4] == 2 and value[8] == 2 and value[0] == 0:
        return 0
    elif value[4] == 2 and value[6] == 2 and value[2] == 0:
        return 2
    elif value[4] == 2 and value[0] == 2 and value[8] == 0:
        return 8

    if value[0] == 2 and value[8] == 2 and value[4] == 0:  # ветка 6
        return 4
    elif value[2] == 2 and value[6] == 2 and value[4] == 0:
        return 4
    
    return 9

def logic_defense(value):
    # Логика защиты (используется после логики атаки если нет возможности завершить игру победой)
    # Если две клетки в линию заняты игроком а третья пустая, то возвращается индекс клетки
    # которую необходимо занять чтобы предотвратить победу игрока.
    # # Если нет такой возможности, то возвращается 9 (такой клетки нет)
    if value[0] == 1 and value[1] == 1 and value[2] == 0:    # ветка 0
        return 2
    elif value[2] == 1 and value[5] == 1 and value[8] == 0:
        return 8
    elif value[8] == 1 and value[7] == 1 and value[6] == 0:
        return 6
    elif value[6] == 1 and value[3] == 1 and value[0] == 0:
        return 0

    if value[1] == 1 and value[2] == 1 and value[0] == 0:  # ветка 1
        return 0
    elif value[5] == 1 and value[8] == 1 and value[2] == 0:
        return 2
    elif value[7] == 1 and value[6] == 1 and value[8] == 0:
        return 8
    elif value[3] == 1 and value[0] == 1 and value[6] == 0:
        return 6

    if value[0] == 1 and value[2] == 1 and value[1] == 0:  # ветка 2
        return 1
    elif value[2] == 1 and value[8] == 1 and value[5] == 0:
        return 5
    elif value[8] == 1 and value[6] == 1 and value[7] == 0:
        return 7
    elif value[6] == 1 and value[0] == 1 and value[3] == 0:
        return 3

    if value[4] == 1 and value[1] == 1 and value[7] == 0:  # ветка 3
        return 7
    elif value[4] == 1 and value[5] == 1 and value[3] == 0:
        return 3
    elif value[4] == 1 and value[7] == 1 and value[1] == 0:
        return 1
    elif value[4] == 1 and value[3] == 1 and value[5] == 0:
        return 5

    if value[1] == 1 and value[7] == 1 and value[4] == 0:  # ветка 4
        return 4
    elif value[3] == 1 and value[5] == 1 and value[4] == 0:
        return 4

    if value[4] == 1 and value[2] == 1 and value[6] == 0:  # ветка 5
        return 6
    elif value[4] == 1 and value[8] == 1 and value[0] == 0:
        return 0
    elif value[4] == 1 and value[6] == 1 and value[2] == 0:
        return 2
    elif value[4] == 1 and value[0] == 1 and value[8] == 0:
        return 8

    if value[0] == 1 and value[8] == 1 and value[4] == 0:  # ветка 6
        return 4
    elif value[2] == 1 and value[6] == 1 and value[4] == 0:
        return 4
    
    return 9

def logic_start_bot(value):
    # Логика игры если начинает бот
    if not (1 in value):
        # 1 ход. Проверяется наличие хотя бы одной 1 в списке клеток, так как еще ни одной нет,
        # то возвращается 4 - индекс центральной клетки.
        return 4
    elif value.count(1) == 1:
        # 3 ход. Подсчитывается количество 1 в клетках, если равно 1, то следовательно 3-й ход в игре (2-й ход бота).
        if value[0] == 1:
            # если 1 (клетка игрока) в углу, то возвращается индекс клетки в углу, следующий по часовой стрелке.
            return 2
        elif value[2] == 1:
            return 8
        elif value[8] == 1:
            return 6
        elif value[6] == 1:
            return 0
                                      
        if value[1] == 1:
            # если 1 (клетка игрока) по центру боковых сторон, то возвращается индекс клетки в противоположном углу
            # (это может быть любой из двух противоположных углов)
            return 6
        elif value[5] == 1:
            return 0
        elif value[7] == 1:
            return 2
        elif value[3] == 1:
            return 8

    elif value.count(1) == 2:
        # 5 ход. Подсчитывается количество 1 в клетках, если равно 2, то следовательно 5-й ход в игре (3-й ход бота).
        temp = logic_attack(value)
        # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
        # то и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
        # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp

    elif value.count(1) == 3:
        # 7 ход. Подсчитывается количество 1 в клетках, если равно 3, то следовательно 7-й ход в игре (4-й ход бота).
        temp = logic_attack(value)
        # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
        # то и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
        # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp

        # Два варианта когда не сработает ни logic_attack() ни logic_defense()
        if value[1] == 0 and value[7] == 0:
            return 1
        elif value[3] == 0 and value[5] == 0:
            return 3

    elif value.count(1) == 4:
        # 9 ход. Подсчитывается количество 1 в клетках, если равно 4, то следовательно 9-й ход в игре (5-й ход бота).
        # Находится последняя пустая клетка и возвращается её индекс
        for i in range(9):
            if value[i] == 0:
                return i

def logic_start_gamer(value):
    # Логика игры если начинает игрок
    if value.count(1) == 1:
        # 2 ход. Подсчитывается количество 1 в клетках, если равно 1, то следовательно 2-й ход в игре (1-й ход бота).
        if value[4] == 1:
            # Проверяется занята ли центральная клетка. Если занята то возвращается индекс любой угловой клети.
            return 0
        # Если центральная клетка свободна то возвращается её индекс.
        return 4
    elif value.count(1) == 2:   # 4 ход
        # 4 ход. Подсчитывается количество 1 в клетках, если равно 2, то следовательно 4-й ход в игре (2-й ход бота).
        if value[4] == 1:
            # Если центральная клетка занята игроком
            temp = logic_defense(value)
            # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
            # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp      
            elif value[8] == 1:
                # Вариант когда не сработает ни logic_attack() ни logic_defense()
                return 2
        else:
            # Если центральная клетка занята ботом
            temp = logic_attack(value)
            # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
            # то и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
            # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp

            # Варианты когда не сработает ни logic_attack() ни logic_defense()
            if value[0]== 1 and value[8] == 1:    # углы напротив друг друга
                return 1 
            elif value[2]== 1 and value[6] == 1:
                return 5

            elif value[0]== 1 and value[5] == 1:  # середина - дальний угол справа
                return 2
            elif value[2]== 1 and value[7] == 1:
                return 5
            elif value[3]== 1 and value[8] == 1:
                return 7
            elif value[1]== 1 and value[6] == 1:
                return 3

            elif value[0]== 1 and value[7] == 1:    # середина - дальний угол слева
                return 3
            elif value[2]== 1 and value[3] == 1:
                return 1
            elif value[8]== 1 and value[1] == 1:
                return 5
            elif value[6]== 1 and value[5] == 1:
                return 7

            elif value[3]== 1 and value[1] == 1:    # центр - центр рядом
                return 0
            elif value[1]== 1 and value[5] == 1:
                return 2
            elif value[5]== 1 and value[7] == 1:
                return 8
            elif value[7]== 1 and value[3] == 1:
                return 6

            elif value[1]== 1 and value[7] == 1:  # центр - центр напротив
                return 5
            elif value[3]== 1 and value[5] == 1:
                return 1
    elif value.count(1) == 3:
        # 6 ход. Подсчитывается количество 1 в клетках, если равно 3, то следовательно 6-й ход в игре (3-й ход бота).
        if value[4] == 1:
            # Если центральная клетка занята игроком
            temp = logic_attack(value)
            # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
            # то и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
            # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp
        else:
            # Если центральная клетка занята ботом
            temp = logic_attack(value)
            # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
            # то и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
            # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
            if -1 < temp < 9:
                return temp

            # Варианты когда не сработает ни logic_attack() ни logic_defense()
            if value[7] == 1 and value[3] == 1 and value[1] == 1: # центр - центр - центр
                return 2
            elif value[3] == 1 and value[1] == 1 and value[5] == 1:
                return 8
            elif value[1] == 1 and value[3] == 1 and value[7] == 1:
                return 6
            elif value[5] == 1 and value[7] == 1 and value[3] == 1:
                return 0

            elif value[3] == 1 and value[1] == 1 and value[8] == 1:   # центр - центр рядом угол напротив
                return 2
            elif value[2] == 1 and value[5] == 1 and value[6] == 1:
                return 8
            elif value[0] == 1 and value[5] == 1 and value[7] == 1:
                return 6
            elif value[2] == 1 and value[7] == 1 and value[3] == 1:
                return 0

            # Если не сработали все условия выше, то возвращается индекс первой попавшейся свободной клетки
            for i in range(9):
                if value[i] == 0:
                    return i
    elif value.count(1) == 4:   # 8 ход
        # 8 ход. Подсчитывается количество 1 в клетках, если равно 4, то следовательно 8-й ход в игре (4-й ход бота).
        temp = logic_attack(value)
        # Проверяется возможность завершить игру победой, если из logic_attack() вернулся индекс от 0 до 8,
        # то и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        # Проверяется возможность предотвратить завершение игры победой игрока. Если есть угроза, то logic_defense()
        # вернет индекс клетки которую необходимо занять и logic_start_bot() вернет этот индекс
        if -1 < temp < 9:
            return temp
        # Если не сработали условия выше, то возвращается индекс первой попавшейся свободной клетки
        for i in range(9):
            if value[i] == 0:
                return i
    elif value.count(1) == 5:
        # Уже не помню нафиг нужен этот шаг проверки, кажется для вывода ничьей
        if value[4] == 1:
            return 0
        return 4


def clear_field():
    # Возвращает все в исходное состояние начала игры
    global b
    global count
    b = [0 for i in range(1, 10)]
    btn_gamer.config(command=start_gamer, relief='raised')
    btn_bot.config(command=start_bot, relief='raised')
    btn1.config(command=press_btn1, image='', relief='raised')
    btn2.config(command=press_btn2, image='', relief='raised')
    btn3.config(command=press_btn3, image='', relief='raised')
    btn4.config(command=press_btn4, image='', relief='raised')
    btn5.config(command=press_btn5, image='', relief='raised')
    btn6.config(command=press_btn6, image='', relief='raised')
    btn7.config(command=press_btn7, image='', relief='raised')
    btn8.config(command=press_btn8, image='', relief='raised')
    btn9.config(command=press_btn9, image='', relief='raised')
    label_finish1.config(text='')
    label_finish2.config(image='')
    count = 0

def start_bot():
    # Нажатие кнопки "Начинает бот"
    global bot
    global b
    global count
    bot = True
    btn_gamer.config(command=0, relief='sunken')
    b[logic_start_bot(b)] = 2
    btn5.config(command=0, image=blue_zero, relief='sunken')
    count += 1

def start_gamer():
    # Нажатие кнопки "Начинает игрок"
    global bot
    bot = False
    btn_bot.config(command=0, relief='sunken')

def finish(champion):
    # В случае победы одной из сторон выводит надпись "Победил" и знак (0 или Х) соответственно
    label_finish1.config(text='Победил:')
    if champion == 2:
        label_finish2.config(image=blue_zero)
    else:
        label_finish2.config(image=red_cross)

def press_button_1_9(index):
    # Основной модуль игры обрабатывающий нажатие кнопок игрового поля
    global bot
    global b
    if bot:
        # Если bot = True (была нажата "Начинает бот")
        btn_1_9[index].config(command=0 , image=red_cross, relief='sunken')
        b[index] = 1
        temp = logic_start_bot(b)
        btn_1_9[temp].config(command=0, image=blue_zero, relief='sunken')
        b[temp] = 2
    else:
        # Если bot = False (была нажата "Начинает игрок")
        btn_1_9[index].config(command=0 , image=red_cross, relief='sunken')
        b[index] = 1
        temp = logic_start_gamer(b)
        btn_1_9[temp].config(command=0, image=blue_zero, relief='sunken')
        b[temp] = 2
    global count
    # Счетчик ходов
    count += 1
    vict, champion = victory(b)
    # После каждого хода проверяет на победу одной из сторон
    if vict:
        # Если victory() вернула True и значение ячейки победителя (1-игрок или 2-бот)
        finish(champion)
    if count == 5:
        # Если количество ходов одной из сторон достигло 5, то ходов больше нет и результат "Ничья"
        label_finish1.config(text='         Ничья!')

b = [0 for i in range(1, 10)]

bot = None
count = 0

def press_btn1():
    # Отпабатывает кнопка соответствующей клетки игрового поля и вызывает основную функцию игры
    index = 0
    press_button_1_9(index)
def press_btn2():
    index = 1
    press_button_1_9(index)
def press_btn3():
    index = 2
    press_button_1_9(index)
def press_btn4():
    index = 3
    press_button_1_9(index)
def press_btn5():
    index = 4
    press_button_1_9(index)
def press_btn6():
    index = 5
    press_button_1_9(index)
def press_btn7():
    index = 6
    press_button_1_9(index)
def press_btn8():
    index = 7
    press_button_1_9(index)
def press_btn9():
    index = 8
    press_button_1_9(index)

import tkinter as tk

win = tk.Tk()
win.title('Крестики-нолики')

w = 480 	# width - ширина
h = 720    # height - высота
sw = win.winfo_screenwidth()    # определяем ширину экрана
x = int((sw - w) / 2)
sh = win.winfo_screenheight()   # определяем высоту экрана
y = int((sh - h) / 2)

win.geometry(f"{w}x{h}+{x}+{y}")
win.resizable(False, False)

red_cross = tk.PhotoImage(file='Task_1/red_cross130.png')
blue_zero = tk.PhotoImage(file='Task_1/blue_zero130.png')

btn_gamer = tk.Button(win, text='Начинает игрок', command=start_gamer, font=('times new roman',14, 'bold'))
raised_01 = tk.Button(win, text='', bg='blue', relief=tk.RAISED, state=tk.DISABLED)
btn_clear = tk.Button(win, text='Очистить поле', command=clear_field , font=('times new roman',14, 'bold'))
raised_02 = tk.Button(win, text='', bg='blue', relief=tk.RAISED, state=tk.DISABLED)
btn_bot = tk.Button(win, text='Начинает бот', command=start_bot, font=('times new roman',14, 'bold'))

btn1 = tk.Button(win, text='', command=press_btn1)
raised_1 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn2 = tk.Button(win, text='', command=press_btn2)
raised_2 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn3 = tk.Button(win, text='', command=press_btn3)
raised_3 = tk.Label (win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED, height=1, font=('Arial',5))

btn4 = tk.Button(win, text='', command=press_btn4)
raised_4 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn5 = tk.Button(win, text='', command=press_btn5)
raised_5 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn6 = tk.Button(win, text='', command=press_btn6)
raised_6 = tk.Label (win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED, height=1, font=('Arial',5))

btn7 = tk.Button(win, text='', command=press_btn7)
raised_7 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn8 = tk.Button(win, text='', command=press_btn8)
raised_8 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn9 = tk.Button(win, text='', command=press_btn9)

label_finish1 = tk.Label(win, text='', font=('times new roman',44, 'bold'))
label_finish2 = tk.Label(win, text='')

btn_gamer.grid(row=0, column=0, sticky='wens')
raised_01.grid(row=0, column=1, sticky='ns')
btn_clear.grid(row=0, column=2, sticky='wens')
raised_02.grid(row=0, column=3, sticky='ns')
btn_bot.grid(row=0, column=4, sticky='wens')

btn1.grid(row=1, column=0, sticky='wens')
raised_1.grid(row=1, column=1, sticky='ns')
btn2.grid(row=1, column=2, sticky='wens')
raised_2.grid(row=1, column=3, sticky='ns')
btn3.grid(row=1, column=4, sticky='wens')
raised_3.grid(row=2, column=0, columnspan=5, sticky='we')

btn4.grid(row=3, column=0, sticky='wens')
raised_4.grid(row=3, column=1, sticky='ns')
btn5.grid(row=3, column=2, sticky='wens')
raised_5.grid(row=3, column=3, sticky='ns')
btn6.grid(row=3, column=4, sticky='wens')
raised_6.grid(row=4, column=0, columnspan=5, sticky='we')

btn7.grid(row=5, column=0, sticky='wens')
raised_7.grid(row=5, column=1, sticky='ns')
btn8.grid(row=5, column=2, sticky='wens')
raised_8.grid(row=5, column=3, sticky='ns')
btn9.grid(row=5, column=4, sticky='wens')

label_finish1.grid(row=6, column=0, columnspan=4)
label_finish2.grid(row=6, column=4, sticky='wens')

btn_1_9 = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=150)
win.grid_rowconfigure(2, minsize=5)
win.grid_rowconfigure(3, minsize=150)
win.grid_rowconfigure(4, minsize=5)
win.grid_rowconfigure(5, minsize=150)
win.grid_rowconfigure(6, minsize=150)
win.grid_rowconfigure(7, minsize=50)
win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=5)
win.grid_columnconfigure(2, minsize=150)
win.grid_columnconfigure(3, minsize=5)
win.grid_columnconfigure(4, minsize=150)

tk.Button(win, text='Закрыть игру', command=win.quit, font=('times new roman',14, 'bold')).grid(row=7, column=0, columnspan=5, sticky='we')

win.mainloop()