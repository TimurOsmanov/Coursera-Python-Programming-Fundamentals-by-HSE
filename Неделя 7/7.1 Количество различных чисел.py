# Дан список чисел, который может содержать до 100000 чисел.Определите, сколько в нем встречается различных чисел.

# Формат ввода
#
# Вводится список целых чисел. Все числа списка находятся на одной строке.
#
# Формат вывода
#
# Выведите ответ на задачу.
n = list(map(int, input().split()))
my_set = set(n)
print(len(my_set))
