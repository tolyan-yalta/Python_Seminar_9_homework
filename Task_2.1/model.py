x = 1
y = 1


def init(a,b):
    global x
    global y
    x = float(a)
    y = float(b)


def summa():
    return x + y

def prod():
    return x * y

def dif():
    return x - y

def div():
    return x / y

def pov():
    return x ** y

op_cod = "[ +  *  -  /  **]"

operations = {'+':summa, '*':prod, '-':dif, '/':div, '**':pov} 