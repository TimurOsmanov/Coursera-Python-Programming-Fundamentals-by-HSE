x = int(input())
y = int(input())
z = int(input())
if x >= y and x >= z:
    print(x)
elif z >= y and z >= x:
    print(z)
elif y >= x and y >= z:
    print(y)
