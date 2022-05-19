# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.
List = list(map(int, input().split()))
last_x = List[-1]
List2 = List.copy()
List3 = []
i = 0
k = 0


def f():
    global i
    if len(List2) == 0:
        return List3
    elif len(List2) % 2 != 0:
        List2.pop()
        i += 1
        f()
    else:
        List2[k], List2[k + 1] = List2[k + 1], List2[k]  # could be deleted, because you can change nex 2 lines
        List3.append(List2[k])
        List3.append(List2[k + 1])
        List2.pop(0)
        List2.pop(0)
        f()


f()
if i == 0:
    print(*List3)
else:
    List3.append(last_x)
    print(*List3)
