# Теорема Лагранжа утверждает, что любое натуральное число можно представить
# в виде суммы четырех точных квадратов. По данному числу n
# найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
# квадраты которых дают в сумме данное число.
n = int(input())
a, b, c, d = 0, 0, 0, 0
i1, i2, i3, i4 = 1, 1, 1, 1


def lagrange(n):
    global i1
    global i2
    global i3
    global i4
    global a
    global b
    global c
    global d
    while n >= i1 ** 2:
        i1 += 1
    a = (i1 - 1)
    if n == a ** 2:
        print(a)
    elif n == a ** 2 + b ** 2:
        print(a, b)
    elif n == a ** 2 + b ** 2 + c ** 2:
        print(a, b, c)
    elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
        print(a, b, c, d)
    else:
        while n - a ** 2 >= i2 ** 2:
            i2 += 1
        b = (i2 - 1)
        if n == a ** 2:
            print(a)
        elif n == a ** 2 + b ** 2:
            print(a, b)
        elif n == a ** 2 + b ** 2 + c ** 2:
            print(a, b, c)
        elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
            print(a, b, c, d)
        else:
            while n - a ** 2 - b ** 2 >= i3 ** 2:
                i3 += 1
            c = (i3 - 1)
            if n == a ** 2:
                print(a)
            elif n == a ** 2 + b ** 2:
                print(a, b)
            elif n == a ** 2 + b ** 2 + c ** 2:
                print(a, b, c)
            elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                print(a, b, c, d)
            else:
                while n - a ** 2 - b ** 2 - c ** 2 >= i4 ** 2:
                    i4 += 1
                d = (i4 - 1)
                if n == a ** 2:
                    print(a)
                elif n == a ** 2 + b ** 2:
                    print(a, b)
                elif n == a ** 2 + b ** 2 + c ** 2:
                    print(a, b, c)
                elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                    print(a, b, c, d)
                else:
                    a -= 1
                    while n - a ** 2 >= i2 ** 2:
                        i2 += 1
                    b = (i2 - 1)
                    if n == a ** 2:
                        print(a)
                    elif n == a ** 2 + b ** 2:
                        print(a, b)
                    elif n == a ** 2 + b ** 2 + c ** 2:
                        print(a, b, c)
                    elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                        print(a, b, c, d)
                    else:
                        while n - a ** 2 - b ** 2 >= i3 ** 2:
                            i3 += 1
                        c = (i3 - 1)
                        if n == a ** 2:
                            print(a)
                        elif n == a ** 2 + b ** 2:
                            print(a, b)
                        elif n == a ** 2 + b ** 2 + c ** 2:
                            print(a, b, c)
                        elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                            print(a, b, c, d)
                        else:
                            while n - a ** 2 - b ** 2 - c ** 2 >= i4 ** 2:
                                i4 += 1
                            d = (i4 - 1)
                            if n == a ** 2:
                                print(a)
                            elif n == a ** 2 + b ** 2:
                                print(a, b)
                            elif n == a ** 2 + b ** 2 + c ** 2:
                                print(a, b, c)
                            elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                                print(a, b, c, d)
                            else:
                                a += 1
                                b -= 2
                                while n - a ** 2 - b ** 2 >= i3 ** 2:
                                    i3 += 1
                                c = (i3 - 1)
                                if n == a ** 2:
                                    print(a)
                                elif n == a ** 2 + b ** 2:
                                    print(a, b)
                                elif n == a ** 2 + b ** 2 + c ** 2:
                                    print(a, b, c)
                                elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                                    print(a, b, c, d)
                                else:
                                    while n - a ** 2 - b ** 2 - c ** 2 >= i4 ** 2:
                                        i4 += 1
                                    d = (i4 - 1)
                                    if n == a ** 2:
                                        print(a)
                                    elif n == a ** 2 + b ** 2:
                                        print(a, b)
                                    elif n == a ** 2 + b ** 2 + c ** 2:
                                        print(a, b, c)
                                    elif n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                                        print(a, b, c, d)


lagrange(n)

#for n in range (1, 10000):
    #lagrange(n)
# Это проверка, ошибка на 9966, убрать из начала первую строчку кода "n = int(input())"
