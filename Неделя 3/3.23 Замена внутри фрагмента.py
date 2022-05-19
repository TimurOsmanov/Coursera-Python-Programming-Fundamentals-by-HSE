# Дана строка. Замените в этой строке
# все появления буквы h на букву H,
# кроме первого и последнего вхождения.
s = str(input())
pos_first = s.find("h")
pos_last = s.rfind("h")
b = s.replace("h", "H")
b = b[(pos_first + 1):pos_last]
print(s[:(pos_first + 1)], b, s[pos_last:], sep='')
