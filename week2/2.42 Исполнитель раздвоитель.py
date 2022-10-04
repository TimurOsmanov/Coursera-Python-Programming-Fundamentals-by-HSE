a, b = int(input()), int(input())
while a > b:
    if a // b == 1 and a % b != 0:
        a -= 1
        print("-1")
    elif a % 2 == 1:
        a -= 1
        print("-1")
    elif a % 2 == 0:
        a /= 2
        print(":2")
