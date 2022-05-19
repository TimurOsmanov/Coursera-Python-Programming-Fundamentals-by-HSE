# Дано действительное положительное число a и целоe число n.
# Вычислите aⁿ. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степерь пользоваться нельзя.
a, n = float(input()), int(input())
b = a
i = 1


def powerpos(a, n):
    global i
    global b
    while i != n:
        a = a * b
        i += 1
    if i == n:
        print(a)


def powerneg(a, n):
    global i
    global b
    while i != n:
        a = a / b
        i -= 1
    if i == n:
        print(a)


def power(a, n):
    if n < 0:
        powerneg(a, n)
    elif n > 0:
        powerpos(a, n)
    else:
        print("1")


power(a, n)
