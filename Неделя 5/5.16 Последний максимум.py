# Найдите наибольшее значение в списке и индекс
# последнего элемента, который имеет данное
# значение за один проход по списку, не
# модифицируя этот список и не используя
# дополнительного списка.
intList = list(map(int, input().split()))
max_x = intList[0]
i = 0
for x in intList:
    if x > max_x:
        max_x = x
    else:
        max_x = max_x
for x in intList[::-1]:
    if x == max_x:
        i = i
        break
    else:
        i += 1
print(max_x, len(intList) - i - 1)
