a = int(input())
b = int(input())
i = 1
mx = 1
while b != 0:
    if a != b:
        a = b
        b = int(input())
    while a == b:
        i += 1
        b = int(input())
    if i > mx:
        mx = i
    i = 1
print(mx)
