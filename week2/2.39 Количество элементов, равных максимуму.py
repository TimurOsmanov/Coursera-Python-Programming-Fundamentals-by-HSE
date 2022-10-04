b = int(input())
max = b
a = int(input())
c = 0
if max > a:
    max = b
    c += 1
elif max < a:
    max = a
    c += 1
elif a == b:
    max = a
    c = 2
while a != 0:
    a = int(input())
    if a == max:
        c += 1
    elif a > max:
        max = a
        c = 1
print(c)
