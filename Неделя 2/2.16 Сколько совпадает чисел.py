a, b, c = int(input()), int(input()), int(input())
# as a result 0 if three of this numbers are not equal,
# 2 if 2 are equal, 3 if 3 are eqaul
if a != b and a != c and b != c:
    print("0")
elif a == b == c:
    print("3")
elif a == b or a == c or b == c:
    print("2")
