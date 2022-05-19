from math import floor, ceil, sqrt
x, n, s1, s2 = int(input()), 0, 0, 0
while x != 0:
    s1 += x
    s2 += x ** 2
    n += 1
    x = int(input())
print(sqrt((s2 - s1 ** 2 / n) / (n - 1)))
