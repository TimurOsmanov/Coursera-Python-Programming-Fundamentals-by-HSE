# Дана последовательность чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.
# Формат ввода
# Вводится последовательность целых чисел,
# оканчивающаяся числом 0 (само число 0 в последовательность
# не входит, а служит как признак ее окончания).
i = 0


def sum():
    x = int(input())
    if x == 0:
        return x
    return x + sum()


print(sum())
