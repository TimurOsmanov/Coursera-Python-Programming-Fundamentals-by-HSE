# Дана строка. Найдите в этой строке второе вхождение
# буквы f и выведите индекс этого вхождения. Если
# буква f в данной строке встречается только один раз,
# выведите число -1, а если не встречается ни разу,
# выведите число -2. При решении этой задачи нельзя использовать метод count.
s = str(input())
pos_0 = 0
pos_s = s.find("f", pos_0)
neg_s = s[::-1]
pos_n_s = s[::-1].find("f", pos_0)
if pos_s == -1:
    print("-2")
elif pos_s >= 0 and ((len(s) - 1) - pos_s == pos_n_s):
    print("-1")
elif pos_s >= 0 and ((len(s) - 1) - pos_s != pos_n_s):
    print(s[(pos_s + 1):].find("f", pos_0) + pos_s + 1)
