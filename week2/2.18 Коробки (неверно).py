a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
if a <= c >= b and b >= a:
    (a, b, c) = (a, b, c)
if a <= b >= c and c >= a:
    (a, c, b) = (a, b, c)
if b <= c >= a and a >= b:
    (b, a, c) = (a, b, c)
if b <= a >= c and c >= b:
    (b, c, a) = (a, b, c)
if c <= b >= a and a >= c:
    (c, a, b) = (a, b, c)
if c <= a >= b and b >= c:
    (c, b, a) = (a, b, c)
if a1 <= c1 >= b1 and b1 >= a1:
    (a1, b1, c1) = (a1, b1, c1)
if a1 <= b1 >= c1 and c1 >= a1:
    (a1, c1, b1) = (a1, b1, c1)
if b1 <= c1 >= a1 and a1 >= b1:
    (b1, a1, c1) = (a1, b1, c1)
if b1 <= a1 >= c1 and c1 >= b1:
    (b1, c1, a1) = (a1, b1, c1)
if c1 <= b1 >= a1 and a1 >= c1:
    (c1, a1, b1) = (a1, b1, c1)
if c1 <= a1 >= b1 and b1 >= c1:
    (c1, b1, a1) = (a1, b1, c1)
if (a1, b1, c1) == (a, b, c):
    print("Boxes are equal")
elif (a1, b1, c1) <= (a, b, c):
    print('The first box is larger than second one')
elif (a1, b1, c1) >= (a, b, c):
    print('The first box is smaller than second one')
else:
    print("Boxes are incomparable")
