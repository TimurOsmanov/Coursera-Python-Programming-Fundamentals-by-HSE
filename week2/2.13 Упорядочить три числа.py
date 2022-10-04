a, b, c = int(input()), int(input()), int(input())
# as a result a, b, c should be printed according to this option a<=b<=c
if a <= b <= c:
    print(a, b, c)
elif c <= a >= b and c >= b:
    print(b, c, a)
elif c <= a >= b and b >= c:
    print(c, b, a)
elif c <= b >= a and a >= c:
    print(c, a, b)
elif c <= b >= a and c >= a:
    print(a, c, b)
else:
    print(b, a, c)
