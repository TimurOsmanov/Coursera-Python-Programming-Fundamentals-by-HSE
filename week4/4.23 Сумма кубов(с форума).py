# Напишите программу, которая представляет переданное натуральное число
# в виде суммы не более чем 7 кубов других натуральных чисел.


def qubes(n, level):
    if level == 0:
        return 0
    q = int(n ** (1 / 3) + 0.00000000000001)
    if q ** 3 == n:
        return str(q ** 3)
    while q > 0:
        if qubes(n - q ** 3, level - 1) != 0:
            return str(q ** 3) + " " + qubes(n - q ** 3, level - 1)
        q -= 1
    return 0


n = int(input())
print(qubes(n, 7))
