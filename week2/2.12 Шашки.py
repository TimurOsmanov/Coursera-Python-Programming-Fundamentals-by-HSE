x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = x1 + y1
b = x2 + y2
if b <= a and y2 < y1 or b % 2 == 1 or a % 2 == 1:
    print("NO")
else:
    print("YES")
