# Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
a, b = float(input()), int(input())
i1 = 0
i2 = 0
i = 0


def sum(a, b):
    global i1
    global i2
    global i
    if i1 - 1 != a:
        i1 += 1
        i += 1
        sum(a, b)
    elif i1 - 1 == a:
        i1 = i1
    if i2 - 1 != b:
        i2 += 1
        i += 1
        sum(a, b)
    elif i2 - 1 == b:
        i2 = i2
    return i - 1 - 1


print(sum(a, b))
