# Даны четыре действительных числа: x₁, y₁, x₂, y₂.
# Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
# Считайте четыре действительных числа и
# выведите результат работы этой функции.
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3 = float(input()), float(input())


def dis(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def perimeter(x1, y1, x2, y2, x3, y3):
    return dis(x1, y1, x2, y2) + dis(x2, y2, x3, y3) + dis(x1, y1, x3, y3)


print(perimeter(x1, y1, x2, y2, x3, y3))
