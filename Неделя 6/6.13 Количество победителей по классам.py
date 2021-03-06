# В условиях предыдущей задачи определите количество школьников, ставших победителями в каждом классе.
# Победителями объявляются все, кто набрал наибольшее число баллов по данному классу.
# Гарантируется, что в каждом классе был хотя бы один участник.
# Формат вывода
# Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу, по 11 классу.
data_in = open('input.txt', 'r', encoding='utf8')
l_1, res = [], []
i1, i2 = 0, 0
for now in data_in:
    a = now.strip().split()
    l_1.append([int(a[2]), int(a[3])])
l_1.sort()
while i1 + 1 < len(l_1):
    max_now = [l_1[i1][0], l_1[i1][1]]
    if l_1[i1][0] == l_1[i1 + 1][0]:
        if l_1[i1][1] > l_1[i1 + 1][1]:
            max_now = [l_1[i1][0], l_1[i1][1]]
            i1 += 1
        else:
            max_now = [l_1[i1 + 1][0], l_1[i1 + 1][1]]
            i1 += 1
    else:
        res.append(max_now)
        max_now = []
        i1 += 1
if l_1[i1 - 1][0] == l_1[i1][0]:
    if l_1[i1 - 1][1] > l_1[i1][1]:
        max_now = [l_1[i1 - 1][0], l_1[i1 - 1][1]]
        res.append(max_now)
    else:
        max_now = [l_1[i1][0], l_1[i1][1]]
        res.append(max_now)
else:
    res.append([l_1[i1][0], l_1[i1][1]])
for x in res:
    print(l_1.count(x), end=' ')
