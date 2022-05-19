# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.
# Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске
# определит максимальное число пользователей, чьи данные можно поместить в архив.
# Формат ввода
# Программа получает на вход в одной строке число S – размер свободного места на диске
# (натуральное, не превышает 10000), и число N – количество пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого пользователя (натуральное, не превышает 1000),
# записанных каждое в отдельной строке.
# Формат вывода
# Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.
m1 = list(map(int, input().split()))
m2 = []
for x in range(m1[1]):
    x = int(input())
    m2.append(x)
m2.sort()
i = m2[0]
i2 = 0
for x in m2:
    if i <= m1[0]:
        i2 += 1
    i += x
print(i2)
