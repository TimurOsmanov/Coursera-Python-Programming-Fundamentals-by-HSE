n, x = float(input()), float(input())
c = 0
sum = 0
while c != n + 1:
    b = float(input())
    sum += x**(n - c) * b
    c += 1
print(sum)
