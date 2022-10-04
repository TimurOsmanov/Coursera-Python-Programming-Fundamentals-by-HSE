m1 = list(map(int, input().split()))
m2 = list(map(int, input().split()))


def intersection(a, b):
    c = []
    for x1 in a:
        for x in b:
            if x1 == x:
                c.append(x)
    print(*c)


intersection(m1, m2)
