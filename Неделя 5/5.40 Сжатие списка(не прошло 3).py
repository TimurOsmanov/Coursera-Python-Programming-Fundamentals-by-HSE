# Дан список целых чисел. Требуется “сжать” его, переместив все
# ненулевые элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть. Порядок ненулевых элементов
# изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
List = list(map(int, input().split()))
i = 0
i2 = -1


def f():
    global i
    global i2
    while i != len(List):
        if List[i] == 0:
            i += 1
        else:
            if List[i] != 0:
                i2 += 1
            while List[i] != List[i2]:
                List[i - 1], List[i] = List[i], List[i - 1]
                i -= 1
            i += 1
            f()


f()
print(*List)
