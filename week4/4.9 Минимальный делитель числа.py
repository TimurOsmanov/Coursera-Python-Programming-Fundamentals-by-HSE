from math import sqrt
n = int(input())


def MinDivisor(n):
    i = 1
    while i <= sqrt(n):
        if n % i == 0 and i > 1:
            break
        i += 1
    else:
        i = n
    return i


print(MinDivisor(n))
