intList = list(map(int, input().split()))
i_pos, i_neg = 0, 0
if len(intList) == 3:
    print(intList[0], intList[1], intList[2])
else:
    for x in intList:
        if x > 0:
            i_pos += 1
        else:
            i_neg += 1
    if i_neg == 0 or i_neg == 1 or i_pos == 0:
        x1 = max(intList)
        intList.pop(intList.index(x1))
        x2 = max(intList)
        intList.pop(intList.index(x2))
        x3 = max(intList)
        print(x1, x2, x3)
    elif i_pos == 1 or i_pos == 2:
        x1 = max(intList)
        intList.pop(intList.index(x1))
        x2 = min(intList)
        intList.pop(intList.index(x2))
        x3 = min(intList)
        print(x1, x2, x3)
    else:
        x1 = max(intList)
        intList.pop(intList.index(x1))
        x2 = max(intList)
        intList.pop(intList.index(x2))
        x3 = max(intList)
        y1 = min(intList)
        intList.pop(intList.index(y1))
        y2 = min(intList)
        if x1 * x2 * x3 > x1 * y1 * y2:
            print(x1, x2, x3)
        else:
            print(x1, y1, y2)
