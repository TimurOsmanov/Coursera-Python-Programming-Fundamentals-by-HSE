a = int(input())
b = int(input())
c = int(input())
z = a**2 + b**2
x = a**2 + c**2
s = c**2 + b**2
if a + b <= c or a + c <= b or b + c <= a:
    print("impossible")
elif a > 0 and b > 0 and c > 0 and z == c**2 or x == b**2 or s == a**2:
    print("rectangular")
elif c**2 > z or a**2 > s or b**2 > x:
    print("obtuse")
elif c**2 < z or a**2 < s or b**2 < x:
    print("acute")
else:
    print("impossible")
