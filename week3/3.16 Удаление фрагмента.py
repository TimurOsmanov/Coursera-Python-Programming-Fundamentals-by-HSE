# Дана строка, в которой буква h встречается
# минимум два раза.Удалите из этой строки
# первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.
s = str(input())
pos_0 = 0
pos_s = s.find("h", pos_0)
neg_s = s[::-1]
pos_n_s = s[::-1].find("h", pos_0)
rpos_n_s = ((len(s) - 1) - pos_n_s) + 1
while pos_0 < pos_s:
    print(s[pos_0], end="")
    pos_0 += 1
while rpos_n_s < len(s):
    print(s[rpos_n_s], end="")
    rpos_n_s += 1
