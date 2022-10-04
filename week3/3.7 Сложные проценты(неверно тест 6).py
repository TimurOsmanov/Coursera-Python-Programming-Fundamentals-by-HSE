from math import floor, ceil, sqrt
P, X, Y, K = float(input()), float(input()), float(input()), float(input())
c = 0
# P - interest rate
# X - amount of bank deposit in rubles ($)
# Y - amount of bank deposit in penny, kopek (cent)
# K - term of deposit
X1 = X * 100
Y1 = Y
d = X1 + Y1
if K == 0:
    print('{0:.0f}'.format(X), '{0:.0f}'.format(Y))
else:
    while c < K:
        X1 = X1 * (100 + P) // 100
        Y1 = Y1 * (100 + P) // 100
        d = X1 + Y1
        c += 1
a = '{0:.0f}'.format(d // 100)
b = '{0:.0f}'.format(d % 100)
print(a, b)
