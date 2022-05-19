# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка
# 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Формат ввода
# Программа получает на вход восемь пар чисел, каждое
# число от 1 до 8 - координаты 8 ферзей.
# Формат вывода
# Если ферзи не бьют друг друга, выведите слово NO,
# иначе выведите YES.
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
l4 = list(map(int, input().split()))
l5 = list(map(int, input().split()))
l6 = list(map(int, input().split()))
l7 = list(map(int, input().split()))
l8 = list(map(int, input().split()))


def Queen_move(a, b):
    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]
    id1 = y0 == y1
    id2 = x0 == x1
    id3 = y0 - y1 == x0 - x1
    id4 = y1 - y0 == x0 - x1
    return id1 or id2 or id3 or id4


def Is_True_Queen_move(a, b):
    if Queen_move(a, b):
        return "YES"
    else:
        return "NO"


l_0 = []
x = 0
l_l = [l1, l2, l1, l3, l1, l4, l1, l5, l1, l6, l1, l7, l1, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l2, l3, l2, l4, l2, l5, l2, l6, l2, l7, l2, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l3, l4, l3, l5, l3, l6, l3, l7, l3, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l4, l5, l4, l6, l4, l7, l4, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l5, l6, l5, l7, l5, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l6, l7, l6, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
x = 0
l_l = [l7, l8]
while x != len(l_l):
    l_0.append(Is_True_Queen_move(l_l[x], l_l[x + 1]))
    x += 2
if l_0.count("YES") >= 1:
    print('YES')
else:
    print('NO')
