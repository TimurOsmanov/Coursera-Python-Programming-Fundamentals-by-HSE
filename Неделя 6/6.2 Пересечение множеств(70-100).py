# Даны два списка, упорядоченных по возрастанию
# (каждый список состоит из различных элементов).
# Найдите пересечение множеств элементов этих списков, то есть
# те числа, которые являются элементами обоих списков.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Решение оформите в виде функции Intersection(A, B).
# Функция должна возвращать список пересечения данных списков
# в порядке возрастания элементов. Модифицировать исходные списки запрещается.
m1 = list(map(int, input().split()))
m2 = list(map(int, input().split()))


def intersection(a, b):
    c1 = a + b
    i = 0
    c = []
    while len(a) > i:
        if c1.count(a[i]) == 1:
            i += 1
        else:
            c.append(a[i])
            i += 1
    print(*c)


intersection(m1, m2)
