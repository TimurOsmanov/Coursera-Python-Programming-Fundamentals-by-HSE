N = int(input())
N0 = N
countmax = 1
while N != 0:
    N = int(input())
    count = 1
    while N == N0:
        count += 1
        N = int(input())
    if countmax < count:
        countmax = count
    N0 = N
print(countmax)
