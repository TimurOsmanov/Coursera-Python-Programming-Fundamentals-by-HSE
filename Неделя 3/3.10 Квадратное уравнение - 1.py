a, b, c = float(input()), float(input()), float(input())
answer = 0
D = b**2 - 4 * a * c
if D < 0:
    answer = "no decisions"
elif D == 0:
    answer = (-b) / (2 * a)
    print(answer)
elif D > 0:
    answer1 = ((-b) + D**(1 / 2)) / (2 * a)
    answer2 = ((-b) - D**(1 / 2)) / (2 * a)
    if answer1 - answer2 > 0:
        print(answer2, answer1)
    else:
        print(answer1, answer2)
