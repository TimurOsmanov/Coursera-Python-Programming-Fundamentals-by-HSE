f0 = 0
f1 = 1
n = int(input())
i = 0
while i < n:
    f1, f0 = f1 + f0, f1
    i += 1
print(f0)
