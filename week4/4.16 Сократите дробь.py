# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два
# других числа p и q таких, что (n / m) =
# (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей
# кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
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


def ReduceFraction(a, b):
    if gcd(a, b) == 1:
        print(a, b)
    else:
        print((g_a // gcd(a, b)), (g_b // gcd(a, b)))


ReduceFraction(a, b)
