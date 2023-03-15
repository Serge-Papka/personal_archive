Сетка = 3  # поле 3*3, 4*4 и т.д
win_lines = 3  # Сколько нужно в ряд для победы


def Logo():
    print('\n           Крестики-Нолики')
    print(f'{win_lines} в ряд. Для ввода напишите координаты(En) от {chr(65)}1 до {chr(63 + Сетка)}{Сетка - 1}')


def show():
    for j in range(Сетка):
        row = ''
        for i in range(Сетка):
            if i and not j:
                row = row + chr(64 + i) + "   "  # Шапка Горизонталь
            elif j and not i:
                if len(str(j)) == 1:
                    row = row + str(j) + "  | "  # Шапка Вертикаль
                else:
                    row = row + str(j) + " | "  # Шапка Вертикаль для 2хзначных чисел
            elif j and i:
                row = row + field[i][j] + " | "
            else:
                row = row + "     "
        print(row)
        print('   ' + "+---" * (Сетка - 1) + "+")


def remove_mistakes(list_):
    miss = [' ', '-', '+', '*', '**', '/', '|', '=', '.', ",", '', '', '', '', ]
    for i in miss:
        while True:
            if list_.count(i):
                list_.remove(i)
            else:
                break
    return list_


def ask():
    while True:
        cords = list(input("\t\t\t\tВаш ход: "))
        cords = remove_mistakes(cords)

        if len(cords) != 2:
            if len(cords) == 3:
                cords[1] = cords[1] + cords[2]
            else:
                print("Введите 2 координаты! ")
                continue

        x, y = cords[0], cords[1]

        if (x.isdigit()) or not (y.isdigit()):
            print("Введите одну букву и одну цифру ")
            continue

        y = int(y)
        x = ord(x) - 64  # ...

        if 1 > x or x > Сетка - 1 or 1 > y or y > Сетка - 1:
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("\t\t\t\tКлетка занята! ")
            continue

        return x, y


def check_win():
    вертикали, горизонтали, диогонали_N, диогонали_И = [], [], [], []

    for i in range(Сетка):
        for j in range(Сетка):
            вертикали.append(field[i][j])
            горизонтали.append(field[j][i])
        вертикали.append('@')
        горизонтали.append('@')

    for j in range(Сетка):  # Сдвиг диогонали / вверх
        for i in range(Сетка - j):
            диогонали_И.append(field[i][Сетка - 1 - j - i])
        диогонали_И.append('@')

    for j in range(1, Сетка):  # Сдвиг диогонали / вправо
        for i in range(Сетка - j):
            диогонали_И.append(field[i + j][Сетка - 1 - i])
        диогонали_И.append('@')

    for j in range(Сетка):  # Сдвиг диогонали \ вверх
        k = 1
        for i in range(Сетка - j - 1, -1, -1):
            диогонали_N.append(field[Сетка - k][i])
            k += 1
        диогонали_N.append('@')

    for j in range(1, Сетка):  # Сдвиг диогонали \ влево
        k = 1
        for i in range(j, Сетка):
            диогонали_N.append(field[Сетка - 1 - i][Сетка - k])
            k += 1
        диогонали_N.append('@')

    сборник = диогонали_N + вертикали + горизонтали + диогонали_И
    win_string = ''.join(сборник)
    if (win_string.find("X" * win_lines) > -1):
        print("\n\t\t\t\tВыиграл X!!!")
        show()
        return True
    if (win_string.find("0" * win_lines)) > -1:
        print("\n\t\t\t\tВыиграл 0!!!")
        show()
        return True
    return False


Сетка += 1  # поле для шапки
Logo()
field = [[" "] * (Сетка) for i in range(Сетка)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("\t\t\t\tХодит крестик!")
    else:
        print("\t\t\t\tХодит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == (Сетка - 1) * (Сетка - 1):
        show()
        print("\n\t\t\t\tНичья!")
        break
    print("\n" * (10 - Сетка))
