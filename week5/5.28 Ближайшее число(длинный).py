# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к  данному числу.
#               Формат ввода
# В первой строке задается одно натуральное число N,
# не превосходящее 1000 – размер массива.
# Во второй строке содержатся N чисел – элементы массива
# (целые числа, не превосходящие по модулю 1000).
# В третьей строке вводится одно целое число x, не
# превосходящее по модулю 1000.
#               Формат вывода
# Вывести значение элемента массива, ближайшее к x.
# Если таких чисел несколько, выведите любое из них.
n = int(input())
b = list(map(int, input().split()))
x = int(input())
b1 = []
i = 0
for z in b:
    if z > 0:
        i += 1
for z in b:
    if i == len(b):
        # all z positive
        if x > 0:
            for d in b:
                c = abs(x - d)
                b1.append(c)
            print(b[b1.index(min(b1))])
        else:
            print(min(b))
        break
    elif i == 0:
        # all z negative
        if x > 0:
            print(max(b))
        else:
            for d in b:
                c = abs(x - d)
                b1.append(c)
            print(b[b1.index(min(b1))])
        break
    else:
        # z are positive and negative
        if x > 0:
            for d in b:
                if d > 0:
                    b1.append(abs(x - d))
                if d < 0:
                    b1.append(abs(x - d))
            print(b[b1.index(min(b1))])
            break
        else:
            for d in b:
                if d > 0:
                    b1.append(abs(x - d))
                if d < 0:
                    b1.append(abs(x - d))
            print(b[b1.index(min(b1))])
        break
