# Напишите программу, которая выбирает из полученной последовательности квадраты
# целых чисел выводит их в обратном порядке. Использовать массив для хранения последовательности не разрешается.
# Формат ввода
# Во входных строках записаны целые числа, по одному в каждой строке. В последней строке записано число 0.
# Формат вывода
# Программа должна вывести элементы полученной последовательности, которые представляют собой квадраты целых
# чисел, в обратном порядке в одну строчку, разделив их пробелами. Если таких нет, программа должна вывести число 0.


def only_square():
    n = int(input())
    global s
    if n != 0:
        only_square()
        if n**(1 / 2) % 1 == 0:
            s += 1
            return print(n, end=' ')


s = 0   ## счетчик точных квадратов
only_square()
if s == 0:
    print(0)
