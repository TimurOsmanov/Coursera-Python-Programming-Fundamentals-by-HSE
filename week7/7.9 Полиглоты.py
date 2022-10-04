# Каждый из N школьников некоторой школы знает Mᵢ языков. Определите,
# какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
#
# Формат ввода
#
# Первая строка входных данных содержит количество школьников N. Далее
# идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков,
# которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
# количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.
#
# Формат вывода
#
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках - список таких языков.
data_in = open('input.txt', 'r', encoding='utf8')
all_lines, i, st_num = [], 0, 0
for now in data_in:
    a = now.strip().split()
    if i == 0:
        st_num = int(a[0])
        i += 1
    else:
        all_lines.append(a[0])
i2, j, set_max, set_all, set_now = 0, 1, set(), set(), set()
st_now = int(all_lines[i2])
list_set = []
while i2 < len(all_lines):
    while st_now - j >= 0:
        i2 += 1
        j += 1
        set_now.add(all_lines[i2])
    list_set.append(set_now)
    set_now = set()
    if i2 + 1 < len(all_lines):
        i2 += 1
        j = 1
        st_now = int(all_lines[i2])
    else:
        i2 += 1
list_set.sort(key=lambda k: len(k))
list_set2 = list_set.copy()
for lists in list_set2:
    set_max |= lists
i3 = 0
set_all = list_set[0]
while i3 < len(list_set) - 1:
    set_all &= list_set[i3]
    i3 += 1
print(len(set_all), *sorted(set_all), len(set_max), *sorted(set_max), sep='\n')
