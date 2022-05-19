n = int(input())
i = 0
c = 1
while i <= n:
    i += 1
    c *= 2
    if n == 1:
        print("0")
        break
    if c >= n:
        print(i)
        break
