from math import floor, ceil, sqrt
a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4 * a * c
if a == b == c == 0:
    print("3")
elif a == b == 0 and c != 0:
    print("0")
elif a == c == 0 and b != 0:
    print("1", "0")
elif b == c == 0 and a != 0:
    print("1", "0")
elif c == 0 and (a != 0 and b != 0):
    answer1 = 0
    answer2 = - b / a
    if answer1 - answer2 > 0:
        print("2", answer2, answer1)
    else:
        print("2", answer1, answer2)
elif b == 0 and (a != 0 and c != 0):
    if c > 0:
        print("0")
    else:
        print("2", - sqrt(- c / a), sqrt(- c / a))
elif a == 0 and (b != 0 and c != 0):
    print("1", - c / b)
elif D == 0:
    print("1", - b / (2 * a))
elif D > 0:
    answer1 = (- b + sqrt(D)) / (2 * a)
    answer2 = (- b - sqrt(D)) / (2 * a)
    if answer1 - answer2 > 0:
        print("2", answer2, answer1)
    else:
        print("2", answer1, answer2)
elif D < 0:
    print("0")
