p, x, y, n = int(input()), int(input()), int(input()), int(input())
i = 0
while i != n:
    i += 1
    k = ((int(x) * 100 + int(y)) * (100 + p)) / 100
    x = k // 100
    y = k % 100
print(int(x), int(y))
