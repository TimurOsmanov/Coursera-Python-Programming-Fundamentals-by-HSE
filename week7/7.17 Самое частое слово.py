# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Формат ввода
#
# Вводится текст.
#
# Формат вывода
#
# Выведите ответ на задачу.
data_in = open('input.txt', 'r', encoding='utf8')
my_dict = dict()
max_n, ans = 0, 0
for line in data_in:
    a = line.strip().split()
    for now in a:
        if now not in my_dict:
            my_dict[now] = 1
        else:
            my_dict[now] += 1
for x in sorted(my_dict):
    if my_dict[x] > max_n:
        max_n, ans = my_dict[x], x
print(ans)
