a = int(input())
b = int(input())
c = int(input())
d = int(input())
a1 = a - c
a2 = c - a
b1 = b - d
b2 = d - b
if (a1 == 1 or a2 == 1 or a == c) and (b1 == 1 or b2 == 1 or b == d):
    print("YES")
else:
    print("NO")
