# Для быстрого вычисления наибольшего общего делителя
# двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b)
a, b = int(input()), int(input())
g_a = a
g_b = b


def gcd(a, b):
    global g_a
    global g_b
    c = a % b
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a
    elif a > b:
        if a % b == 0:
            return b
        elif b % c == 0:
            return c
        else:
            a = b
            b = c
            return gcd(a, b)
    elif b > a:
        a = g_b
        b = g_a
        return gcd(a, b)


print(gcd(a, b))
