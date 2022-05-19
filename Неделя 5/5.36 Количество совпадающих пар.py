# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
l1 = list(map(int, input().split()))
l2 = []
l3 = []


def f1(l1):
    global l2
    i = -1
    while i != len(l1) - 1:
        i += 1
        if l1.count(l1[i]) > 1:
            l2.append(l1[i])
    return l2


f1(l1)
l3 = l2.copy()


def f2(l3):
    i = -1
    while i != len(l3) - 1:
        i += 1
        if l3.count(l3[i]) > 1:
            l3.pop(i)
            f2(l3)


f2(l3)
i = 0
for x in l3:
    a = l2.count(x)
    while a != 1:
        i += a - 1
        a -= 1
print(i)
