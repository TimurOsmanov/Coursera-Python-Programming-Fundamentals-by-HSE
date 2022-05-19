# Головоломка “Ханойские башни” состоит из трех стержней,
# пронумерованных числами 1, 2, 3. На стержень 1 надета
# пирамидка из n дисков различного диаметра в порядке
# убывания диаметра (снизу находится самый большой диск,
# а сверху — самый маленький). Диски можно перекладывать
# с одного стержня на другой по одному, при этом диск
# нельзя класть на диск меньшего диаметра. Необходимо
# переложить всю пирамидку со стержня 1 на стержень
# 3 за минимальное число перекладываний.
#
# Напишите программу, которая решает головоломку;
# для данного числа дисков n печатает последовательность
# перекладываний в формате a b c, где a — номер перекладываемого
# диска, b — номер стержня с которого снимается данный диск,
# c — номер стержня на который надевается данный диск.
#
# Например, строка 1 2 3 означает перемещение диска номер 1
# со стержня 2 на стержень 3. В одной строке печатается одна
# команда. Диски пронумерованы числами от 1 до n в порядке
# возрастания диаметров.
#
# Программа должна вывести минимальный (по количеству
# произведенных операций) способ перекладывания пирамидки
# из данного числа дисков.
#
# Указание: подумайте, как переложить пирамидку из одного диска?
# Из двух дисков? Из трех дисков? Из четырех дисков? Пусть мы научились
# перекладывать пирамидку из n дисков с произвольного стержня
# на любой другой, как переложить пирамидку из n+1 диска,
# если можно пользоваться решением для n дисков.
#
# Напишите функцию move (n, x, y), которая печатает последовательность
# перекладываний дисков для перемещения пирамидки высоты n со
# стержня номер x на стержень номер y.
# Вводится натуральное число — количество дисков.

n = int(input())
x = 1
y = 2
z = 3


def x_to_y(n, x, y):
    l = [n, x, y]
    if n == 1:
        print(*l)
    else:
        x_to_z(n - 1, x, z)
        print(*l)
        z_to_y(n - 1, z, y)


def x_to_z(n, x, z):
    l = [n, x, z]
    if n == 1:
        print(*l)
    else:
        x_to_y(n - 1, x, y)
        print(*l)
        y_to_z(n - 1, y, z)


def y_to_x(n, y, x):
    l = [n, y, x]
    if n == 1:
        print(*l)
    else:
        y_to_z(n - 1, y, z)
        print(*l)
        z_to_x(n - 1, z, x)


def y_to_z(n, y, z):
    l = [n, y, z]
    if n == 1:
        print(*l)
    else:
        y_to_x(n - 1, y, x)
        print(*l)
        x_to_z(n - 1, x, z)


def z_to_x(n, z, x):
    l = [n, z, x]
    if n == 1:
        print(*l)
    else:
        z_to_y(n - 1, z, y)
        print(*l)
        y_to_x(n - 1, y, x)


def z_to_y(n, z, y):
    l = [n, z, y]
    if n == 1:
        print(*l)
    else:
        z_to_x(n - 1, z, x)
        print(*l)
        x_to_y(n - 1, x, y)


x_to_z(n, x, z)
