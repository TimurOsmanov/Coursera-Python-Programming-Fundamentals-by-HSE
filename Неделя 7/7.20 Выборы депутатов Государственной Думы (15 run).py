# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
# определяет следующий алгоритм пропорционального распределения мест в парламенте.
#
# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию и подсчитывается сумма голосов,
# поданных за все партии. Эта сумма делится на 450, получается величина, называемая
# “первое избирательное частное” (смысл первого избирательного частного - это количество голосов избирателей,
# которое необходимо набрать для получения одного места в парламенте). Далее каждая партия получает столько
# мест в парламенте, чему равна целая часть от деления числа голосов за данную партию на первое избирательное частное.
# Если после первого раунда распределения мест сумма количества мест, отданных партиям, меньше 450,
# то оставшиеся места передаются по одному партиям, в порядке убывания дробной части частного от деления числа
# голосов за данную партию на первое избирательное частное. Если же для двух партий эти дробные части равны,
# то преимущество отдается той партии, которая получила большее число голосов.
#
# Формат ввода
#
# На вход программе подается список партий, участвовавших в выборах. Каждая строка входного файла
# содержит название партии (строка, возможно, содержащая пробелы), затем, через пробел, количество голосов,
# полученных данной партией – число, не превосходящее 10⁸.
#
# Формат вывода
#
# Программа должна вывести названия всех партий и количество голосов в парламенте, полученных данной партией.
# Названия необходимо выводить в том же порядке, в котором они шли во входных данных.
data_in = open('input.txt', 'r', encoding='utf8')
my_dict = dict()
all_votes, quotient, res = 0, 0, []
s, c, i = 0, str(), 0
for line in data_in:
    a = line.strip().split()
    if len(a) > 0:
        b, d = int(a[-1]), a[:-1]
        for m in d:
            c += m + ' '
        c = c.strip()
        if c not in my_dict:
            my_dict[c] = b
        else:
            my_dict[c] += b
        c = str()
for now in my_dict:
    all_votes += my_dict[now]
quotient = (all_votes / 450)
for now in my_dict:
    res.append((my_dict[now] % quotient, now))
    my_dict[now] = my_dict[now] // quotient
    s += my_dict[now]
res.sort(reverse=True)
while s != 450:
    if int(res[i][0] * 100000000) != int(res[i + 1][0] * 100000000):
        my_dict[res[i][1]] += 1
        i += 1
        s += 1
    else:
        if my_dict[res[i][1]] > my_dict[res[i + 1][1]]:
            my_dict[res[i][1]] += 1
        else:
            my_dict[res[i + 1][1]] += 1
        i += 1
        s += 1
for x in my_dict:
    print(x, int(my_dict[x]))
