# Дано действительное положительное число a и целое
# неотрицательное число n. Вычислите aⁿ, не используя
# циклы и стандартную функцию pow, но используя
# рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).
a, n = float(input()), int(input())
i = 1


def power(a, n):
    global i
    x = a * a**(i - 1)
    if n == 0:
        print("1")
    elif i == n:
        print(x)
    elif i != n:
        i += 1
        power(a, n)


power(a, n)
