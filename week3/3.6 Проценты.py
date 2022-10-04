from math import floor, ceil, sqrt
P, X, Y = float(input()), float(input()), float(input())
# P - interest rate
# X - amount of bank deposit in rubles ($)
# Y - amount of bank deposit in penny, kopek (cent)
a = '{0:.0f}'.format(((X * 100 + Y) * (100 + P)) // 10000)
b = '{0:.0f}'.format(((X * 100 + Y) * (100 + P)) % 10000 // 100)
print(a, b)
