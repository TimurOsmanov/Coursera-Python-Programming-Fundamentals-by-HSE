from math import floor, ceil, sqrt
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
# ax + by = e
# cx + dy = f
# system of linear equations
y = (f - e * c / a) / (d - b * c / a)
x = (e - b * y) / a
print(x, y)
