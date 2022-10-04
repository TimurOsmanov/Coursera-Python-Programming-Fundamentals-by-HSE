n = int(input())
a = b = c = d = e = f = g = 0


def Lagrange_cub_7(n):
    global a
    a = int(n**(1/3) + 0.00000000000001)
    if a**3 == n:
        print(a**3)
    else:
        Lagrange_cub_6(n)


def Lagrange_cub_6(n):
    global a
    global b
    n2 = n - a**3
    b = int(n2**(1/3) + 0.00000000000001)
    if a**3 + b**3 == n:
        print(a**3, b**3)
    else:
        Lagrange_cub_5(n)


def Lagrange_cub_5(n):
    global a
    global b
    n3 = n - a**3 - b**3
    c = int(n3**(1/3) + 0.00000000000001)
    if a < 0:
        print("0")
    else:
        if a**3 + b**3 + c**3 == n:
            print(a**3, b**3, c**3)
        else:
            n4 = n3 - c**3
            d = int(n4**(1/3) + 0.00000000000001)
            if a**3 + b**3 + c**3 + d**3 == n:
                print(a**3, b**3, c**3, d**3)
            else:
                n5 = n4 - d**3
                e = int(n5**(1/3) + 0.00000000000001)
                if a**3 + b**3 + c**3 + d**3 + e**3 == n:
                    print(a**3, b**3, c**3, d**3, e**3)
                else:
                    n6 = n5 - e**3
                    f = int(n6**(1/3) + 0.00000000000001)
                    if a**3 + b**3 + c**3 + d**3 + e**3 + f**3 == n:
                        print(a**3, b**3, c**3, d**3, e**3, f**3)
                    else:
                        n7 = n6 - f**3
                        g = int(n7**(1/3) + 0.00000000000001)
                        if a**3 + b**3 + c**3 + d**3 + e**3 + f**3 + g**3 == n:
                            print(a**3, b**3, c**3, d**3, e**3, f**3, g**3)
                        else:
                            a -= 1
                            Lagrange_cub_5(n)


Lagrange_cub_7(n)
