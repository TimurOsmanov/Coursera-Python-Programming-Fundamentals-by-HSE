# Напишите функцию min4(a, b, c, d), вычисляющую
# минимум четырех чисел, которая не содержит
# инструкции if, а использует стандартную
# функцию min от двух чисел. Считайте
# четыре целых числа и выведите их минимум.
a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min4(a, b, c, d):
    ans1_1 = min(a, b)
    ans1_3 = min(c, d)
    ans3_1 = min(ans1_1, ans1_3)
    return ans3_1


print(min4(a, b, c, d))
