# Даны четыре действительных числа: x₁, y₁, x₂, y₂.
# Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
# Считайте четыре действительных числа и
# выведите результат работы этой функции.
from math import fabs, sqrt
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())


def distance(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        ans = 0
    elif x1 == x2:
        ans = fabs(fabs(y1) - fabs(y2))
    elif y1 == y2:
        ans = fabs(fabs(x1) - fabs(x2))
    else:
        ans = sqrt((fabs(x1) + fabs(x2))**2 + (fabs(y1) + fabs(y2))**2)
    return ans


print(distance(x1, y1, x2, y2))
