num_1 = 0
num_2 = 0
oper = ''

def inp(num_1, num_2):
    if 'j' in num_1:
        num_1 = complex(num_1)
    else:
        num_1 = float(num_1)
    if 'j' in num_2:
        num_2 = complex(num_2)
    else:
        num_2 = float(num_2)
    return (num_1, num_2)


def inp2():
    global num_1
    global num_2
    global oper
    num_1 = input('Введите число 1: ')
    num_2 = input('Введите число 2: ')
    if 'j' in num_1:
        num_1 = complex(num_1)
    else:
        num_1 = float(num_1)
    if 'j' in num_2:
        num_2 = complex(num_2)
    else:
        num_2 = float(num_2)
    oper = input('Введите оператор (*, /, -, +): ')
    return (num_1, num_2, oper)