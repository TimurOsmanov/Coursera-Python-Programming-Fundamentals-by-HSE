from itertools import permutations
# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.
#
# Формат ввода
#
# Задано 1 число: N (0<N<10).
#
# Формат вывода
#
# Необходимо вывести все перестановки чисел от 1 до N в лексикографическом порядке.
# Перестановки выводятся по одной в строке, числа в перестановке выводятся без пробелов.
print(
    *map(
        lambda z: ''.join(z),
        permutations(
            ''.join(
                map(
                    str,
                    (range(1, int(input()) + 1))
                )
            )
        )
    ),
    sep='\n'
)
