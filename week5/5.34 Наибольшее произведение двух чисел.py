# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых
# максимально. Выведите эти числа в порядке неубывания.
# Решение должно иметь сложность O(n), где n - размер списка.
# То есть сортировку использовать нельзя.
m = list(map(int, input().split()))
m_pos = []
m_neg = []
x_max = 0
x_max_2 = 0

i_pos = 0
i_neg = 0
x_pos1 = 0
x_pos2 = 0
x_neg1 = 0
x_neg2 = 0


for x in m:
    if x > 0:
        i_pos += 1
    else:
        i_neg += 1
if i_neg == 0 or i_neg == 1:
    x_max = max(m)
    m.pop(m.index(x_max))
    x_max_2 = max(m)
    print(x_max, x_max_2)
elif i_pos == 0 or i_pos == 1:
    x_max = min(m)
    m.pop(m.index(x_max))
    x_max_2 = min(m)
    print(x_max, x_max_2)
else:
    for x in m:
        if x > 0:
            m_pos.append(x)
        else:
            m_neg.append(x)
    x_pos1 = max(m_pos)
    m_pos.pop(m_pos.index(x_pos1))
    x_pos2 = max(m_pos)
    x_neg1 = min(m_neg)
    m_neg.pop(m_neg.index(x_neg1))
    x_neg2 = min(m_neg)
    if x_pos2 * x_pos1 > x_neg2 * x_neg1:
        print(x_pos2, x_pos1)
    else:
        print(x_neg1, x_neg2)
