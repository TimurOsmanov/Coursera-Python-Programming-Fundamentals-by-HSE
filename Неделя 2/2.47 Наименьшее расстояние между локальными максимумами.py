a1, a2, a3 = int(input()), int(input()), int(input())
i, count, s_min = 3, 0, 0
while a3 != 0:
    if a1 < a2 > a3:
        count += 1
        if count == 1:
            i_max = i
        elif count == 2:
            s = i - i_max
            s_min = s
            i_max = i
        elif count > 2:
            s = i - i_max
            if s < s_min:
                s_min = s
            i_max = i
    a1 = a2
    a2 = a3
    a3 = int(input())
    i += 1
print(s_min)
