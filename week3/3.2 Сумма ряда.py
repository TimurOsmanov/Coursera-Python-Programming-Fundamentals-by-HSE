n = int(input())
i = 1
c = 1
while c < n:
    i = i + 1 / (1 + c) ** 2
    c += 1
print('{0:.5f}'.format(i))
