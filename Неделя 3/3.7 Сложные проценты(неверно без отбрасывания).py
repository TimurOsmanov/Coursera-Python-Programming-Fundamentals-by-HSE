from math import floor, ceil, sqrt
P, X, Y, K = float(input()), float(input()), float(input()), float(input())
c = 1
# P - interest rate
# X - amount of bank deposit in rubles ($)
# Y - amount of bank deposit in penny, kopek (cent)
# K - term of deposit
v = (X * 100 + Y) * (100 + P)
while c < K:
    v = v * (100 + P)
    c += 1
a = '{0:.0f}'.format(v // 100**(c + 1))
b = '{0:.0f}'.format(v % 100**(c + 1) // 100**c)
print(a, b)
