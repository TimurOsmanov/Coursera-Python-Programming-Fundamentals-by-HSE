villages_qty = int(input())
v = list(map(int, input().split()))
bunkers_qty = int(input())
b = list(map(int, input().split()))
v1, b1, res = v.copy(), b.copy(), []
i, i1, j, j1 = 1, 1, 0, 0
v1.sort(), b1.sort()
while j < len(v1):
    if j1 < len(b1) - 1:
        if abs(b1[j1] - v1[j]) > abs(b1[j1 + 1] - v1[j]):
            j1 += 1
        else:
            res.append([v.index(v1[j]) + 1, b.index(b1[j1]) + 1])
            j += 1
    else:
        res.append([v.index(v1[j]) + 1, b.index(b1[j1]) + 1])
        j += 1
res.sort()
for x in res:
    print(x[1], end=' ')
