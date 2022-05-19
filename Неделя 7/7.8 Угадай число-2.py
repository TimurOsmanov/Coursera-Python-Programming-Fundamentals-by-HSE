# Август и Беатриса продолжают играть в игру, но Август начал жульничать. На каждый из вопросов Беатрисы он
# выбирает такой вариант ответа YES или NO, чтобы множество возможных задуманных чисел оставалось как можно больше.
# Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то Август ответит NO,
# а если Беатриса спросит про 1, 2, 3, то Август ответит YES. Если же Бетриса в своем вопросе перечисляет ровно
# половину из задуманных чисел, то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает
# все предыдущие вопросы Беатрисы и свои ответы на них, то есть множество возможных задуманных чисел уменьшается.
#
# Формат ввода
#
# Вам дана последовательность вопросов Беатрисы. Приведите ответы Августа на них. Первая строка входных данных
# содержит число n — наибольшее число, которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# Последняя строка входных данных содержит одно слово HELP.
#
# Формат вывода
#
# Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. После этого выведите (через пробел,
# в порядке возрастания) все числа, которые мог загадать Август после ответа на всевопросы Беатрисы.
data_in = open('input.txt', 'r', encoding='utf8')
n, i = 0, 0
all_set, now_set = set(), set()
for now in data_in:
    a = now.strip().split()
    if i == 0:
        n = int(a[0])
        i += 1
        for x in range(1, n + 1):
            all_set.add(x)
    else:
        if a == ['HELP']:
            print(*sorted(all_set))
        else:
            now_set = set()
            for y in a:
                now_set.add(int(y))
            if len(now_set & all_set) * 2 <= len(all_set):
                print('NO')
                all_set -= now_set
            else:
                print('YES')
                all_set &= now_set
