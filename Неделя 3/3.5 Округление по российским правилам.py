from math import floor, ceil, sqrt
a = float(input())
if (a - int(a)) - 0.5 < 0:
    print(floor(a))
else:
    print(ceil(a))
