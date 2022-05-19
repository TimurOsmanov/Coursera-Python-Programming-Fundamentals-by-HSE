# Выведите значение наименьшего из всех положительных
# элементов в списке. Известно, что в списке есть
# хотя бы один положительный элемент, а значения всех
# элементов списка по модулю не превосходят 1000.
intList = list(map(int, input().split()))
i = 0
for x in intList:
    if x > 0:
        i = i
        break
    else:
        i += 1
z = intList[i]
for x in intList:
    if x > 0:
        if x > z:
            z = z
        else:
            z = x
print(z)
