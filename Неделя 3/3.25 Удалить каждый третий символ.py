# Дана строка. Удалите из нее все символы,
# чьи индексы делятся на 3.Символы
# строки нумеруются, начиная с нуля.
s = str(input())
sMod = str()
i = 0
while i < (len(s)):
    if i % 3 == 0:
        i += 1
    else:
        sMod = sMod + s[i]
        i += 1
print(sMod)
