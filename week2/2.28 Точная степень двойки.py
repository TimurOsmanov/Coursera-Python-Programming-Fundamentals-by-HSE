n = int(input())
i = 1
while i <= n:
    i = i * 2
    if n == 1:
        print("YES")
        break
    elif n == i:
        print("YES")
        break
else:
    print("NO")
