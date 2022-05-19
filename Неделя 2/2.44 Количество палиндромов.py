n = int(input())
i = 0
a = 0
d = 1000
e = 10000
f = 100000
while n > i:
    i += 1
    if i < 10:
        a += 1
    elif 10 < i < 100 and i % 10 == i // 10:
        a += 1
    elif 100 < i < 1000 and i % 10 == i // 100:
        a += 1
    elif d < i < e and (i % 10 == i // d) and (i // 100 % 10 == i // 10 % 10):
        a += 1
    elif e < i < f and i % 10 == i // e and i // d % 10 == i // 10 % 10:
        a += 1
print(a)
