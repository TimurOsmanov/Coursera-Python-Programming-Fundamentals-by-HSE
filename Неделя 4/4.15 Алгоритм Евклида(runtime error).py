# Для быстрого вычисления наибольшего общего делителя
# двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
a, b = int(input()), int(input())
g_a = a
g_b = b


def gcd(a, b):
    global g_a
    global g_b
    if g_a == 0:
        return g_b
    elif g_b == 0:
        return g_a
    elif abs(g_a) == abs(g_b):
        return abs(g_a)
    elif abs(g_a) > abs(g_b):
        if abs(g_a) % abs(g_b) == 0:
            return abs(g_b)
        elif abs(g_a) % abs(g_b) != 0:
            if abs(g_a) % (b - 1) == 0 and abs(g_b) % (b - 1) == 0:
                return b - 1
            else:
                return gcd(a, b - 1)
    elif abs(g_b) > abs(g_a):
        if abs(g_b) % abs(g_a) == 0:
            return abs(g_a)
        elif abs(g_b) % abs(g_a) != 0:
            if abs(g_b) % (a - 1) == 0 and abs(g_a) % (a - 1) == 0:
                return a - 1
            else:
                return gcd(a - 1, b)


print(gcd(a, b))
