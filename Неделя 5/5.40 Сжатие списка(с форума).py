# Дан список целых чисел. Требуется “сжать” его, переместив все
# ненулевые элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть. Порядок ненулевых элементов
# изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
lst = list(map(int, input().split()))
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))
print(*lst)
