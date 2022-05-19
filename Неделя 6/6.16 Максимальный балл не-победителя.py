# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники,
# которые набрали наибольший балл среди всех участников в данном классе.
#
# Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.
#
# Формат вывода
#
# Выведите три целых числа.
data_in = open('input.txt', 'r', encoding='utf8')
data_out = open('output.txt', 'w', encoding='utf8')
units, res = [], []
i, i2 = 0, 0
for now in data_in:
    a = now.strip().split()
    units.append([int(a[-2]), int(a[-1])])
units.sort(reverse=True)
while i < len(units) - 1:
    if units[i][0] == units[i + 1][0]:
        if units[i][1] == units[i + 1][1]:
            i += 1
        else:
            res.append(units[i + 1])
            if len(res) == 3:
                break
            i += 1
            while units[i][0] == units[i + 1][0]:
                i += 1

    else:
        i += 1
res.sort()
for x in res:
    print(x[1], end=" ")
