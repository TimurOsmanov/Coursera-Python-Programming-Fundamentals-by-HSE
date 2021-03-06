# Политическая жизнь одной страны очень оживленная. В стране действует K политических партий,
# каждая из которых регулярно объявляет национальную забастовку. Дни, когда хотя бы одна из партий
# объявляет забастовку, при условии, что это не суббота или воскресенье (когда и так никто не работает),
# наносят большой ущерб экономике страны. i-я партия объявляет забастовки строго каждые bᵢ дней,
# начиная с дня с номером aᵢ. То есть i-я партия объявляет забастовки в дни aᵢ, aᵢ+bᵢ, aᵢ+2bᵢ и т.д.
# Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной
# забастовкой. В календаре страны N дней, пронумерованных от 1 до N. Первый день года является
# понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.
#
# Формат ввода
#
# Программа получает на вход число дней в году N (1≤N≤10⁶) и число политических партий
# K (1≤K≤100). Далее идет K строк, описывающие графики проведения забастовок.i-я строка
# содержит числа aᵢ и bᵢ (1≤aᵢ,bᵢ≤N).
#
# Формат вывода
#
# Выведите единственное число: количество забастовок, произошедших в течение года.
K, N, i, parties = 0, 0, 0, []
data_in = open('input.txt', 'r', encoding='utf8')
for now in data_in:
    a = now.strip().split()
    if i == 0:
        N, K = int(a[0]), int(a[1])
        i += 1
    else:
        parties.append([int(a[0]), int(a[1])])
all_days, vacation, strikes, m = [], [], [], set()
for x in range(1, N + 1):
    all_days.append(x)
i = 0
for y in all_days:
    i += 1
    if i == 6:
        vacation.append(y)
    elif i == 7:
        i = 0
        vacation.append(y)
work_days = set(all_days) - set(vacation)
for z in parties:
    c = set((all_days[z[0] - 1::z[1]]))
    strikes.append(c)
for u in strikes:
    m |= u
print(len(m - set(vacation)))
