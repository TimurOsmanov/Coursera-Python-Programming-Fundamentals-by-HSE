# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.
n = int(input())
i = 0


def j(n):
    if n == 1:
        print(1)
    else:
        j(n - 1)
        for x in range(1, n + 1):
            print(x, end="")
        print()


j(n)
