n = int(input())
f0 = 0
f1 = 1
i = 0
while f0 < n:
    f1, f0 = f0 + f1, f1
    i += 1
if f0 == n:
    print(i)
else:
    print(-1)
