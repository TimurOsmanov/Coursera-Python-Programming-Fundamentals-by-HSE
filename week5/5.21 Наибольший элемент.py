# Дан список чисел. Выведите значение наибольшего
# элемента в списке, а затем индекс этого элемента
# в списке. Если наибольших элементов несколько,
# выведите их значение и индекс первого из них.

intList = list(map(int, input().split()))
max_x = intList[0]
i = 0
for x in intList:
    if x > max_x:
        max_x = x
    else:
        max_x = max_x
for x in intList:
    if x == max_x:
        i = i
        break
    else:
        i += 1
print(max_x, i)
