n = int(input())
i = 1
print("1", end=" ")
while i <= n:
    i = i * 2
    if n >= i:
        print(i, end=" ")
