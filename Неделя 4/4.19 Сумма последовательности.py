# Дана последовательность чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.
# Формат ввода
# Вводится последовательность целых чисел,
# оканчивающаяся числом 0 (само число 0 в последовательность
# не входит, а служит как признак ее окончания).
i = 0


def sum_sequence():
    n = int(input())
    global i
    if n != 0:
        sum_sequence()
        i += n
        return i
    elif n == 0:
        return 0


print(sum_sequence())
