a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if (a <= d or b <= d) and (b <= e or a <= e):
    print("YES")
elif (a <= d or c <= d) and (c <= e or a <= e):
    print("YES")
elif (c <= d or b <= d) and (b <= e or c <= e):
    print("YES")
else:
    print("NO")
