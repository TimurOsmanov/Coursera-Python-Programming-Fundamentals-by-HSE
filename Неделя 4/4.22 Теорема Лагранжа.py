from math import sqrt
# Теорема Лагранжа утверждает, что любое натуральное число можно представить
# в виде суммы четырех точных квадратов. По данному числу n
# найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
# квадраты которых дают в сумме данное число.
n = int(input())
a, b, c, d = 0, 0, 0, 0


def lagrange4(n):
    global a
    if n == a**2 + b**2 + c**2 + d**2:  # стоп-условие выхода из рекурсии
        print(a, b, c, d)
    else:
        a = int(sqrt(n))
        if n == a ** 2:
            print(a)
        else:
            lagrange3(n)


def lagrange3(n):
    global a
    b = int(sqrt(n - a ** 2))
    if n == a ** 2 + b ** 2:
        print(a, b)
    else:
        c = int(sqrt(n - a ** 2 - b ** 2))
        if n == a ** 2 + b ** 2 + c ** 2:
            print(a, b, c)
        else:
            d = int(sqrt(n - a ** 2 - b ** 2 - c ** 2))
            if n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                print(a, b, c, d)
            else:
                a -= 1
                lagrange3(n)


lagrange4(n)
