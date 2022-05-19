a, n = float(input()), int(input())


def pow(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return pow(a, n // 2)**2
        return pow(a, n-1) * a


print(pow(a, n))