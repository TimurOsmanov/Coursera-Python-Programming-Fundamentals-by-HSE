# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
# Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
# Использовать встроенные функции сортировки нельзя.
A = list(map(int, input().split()))
grades = [0] * 101


def CountSort(A):
    for now in A:
        grades[now] += 1
    for grade in range(len(grades)):
        for i in range(grades[grade]):
            print(grade, end=' ')


CountSort(A)
