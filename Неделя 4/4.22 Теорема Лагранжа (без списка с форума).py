# Теорема Лагранжа утверждает, что любое натуральное число можно представить
# в виде суммы четырех точных квадратов. По данному числу n
# найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
# квадраты которых дают в сумме данное число.


import math


def Lagr(n) -> object:
    i = 0
    n2 = int(math.sqrt(n))
    if math.sqrt(n) % 1 == 0:
        return n2
    n1 = str(n2) + ' ' + str(Lagr(n - n2 ** 2))
    while n1.count(' ') > 3:
        i += 1
    n2 = int(math.sqrt(n - i))
    n1 = str(n2) + ' ' + str(Lagr(n - n2 ** 2))
    return n1


n = int(input())
print(Lagr(n))

