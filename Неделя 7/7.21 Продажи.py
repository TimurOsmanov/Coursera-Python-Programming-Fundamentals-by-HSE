# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида
# Покупатель товар количество, где
# Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя
# подсчитайте количество приобретенных им единиц каждого вида товаров.
#
# Формат ввода
#
# Вводятся сведения о покупках в указанном формате.
#
# Формат вывода
#
# Выведите список всех покупателей в лексикографическом порядке,после имени каждого покупателя
# выведите двоеточие, затем выведите список названий всех приобретенных данным покупателем товаров
# в лексикографическом порядке, после названия каждого товара выведите количество единиц товара,
# приобретенных данным покупателем.Информация о каждом товаре выводится в отдельной строке.
data_in = open('input.txt', 'r', encoding='utf8')
b = dict()
for line in data_in:
    a = line.strip().split()
    if len(a) > 0:
        if a[0] not in b:
            b[a[0]] = {a[1]: int(a[2])}
        else:
            if a[1] not in b[a[0]]:
                b[a[0]][a[1]] = int(a[2])
            else:
                b[a[0]][a[1]] += int(a[2])
for x in sorted(b):
    print(x, ":", sep='')
    for z in sorted(b[x]):
        print(z, b[x][z])
