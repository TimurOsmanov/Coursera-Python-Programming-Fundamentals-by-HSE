# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
List = list(map(int, input().split()))
for x in List:
    while List.count(x) > 1:
        List.pop(List.index(x))
print(len(List))
