# Формат входных данных аналогичен предыдущей задаче.
# Выведите список всех партий, участвовавших в выборах,
# отсортировав его в порядке убывания количества голосов избирателей,
# а при равном количестве голосов - в лексикографическом порядке.
data_in = open('input.txt', 'r', encoding='utf8')
parties, votes, ans = [], [], []
i, sum_votes = 0, 0
for now in data_in:
    a = now.strip().split()
    if a[0] != 'PARTIES:' and a[0] != 'VOTES:':
        if i == 1:
            parties.append(a)
        else:
            votes.append(a)
    else:
        i += 1
res = [0] * len(parties)
for now1 in votes:
    res[parties.index(now1)] += 1
i = 0
for now2 in res:
    ans.append([-now2, parties[i]])
    i += 1
ans.sort()
for x in ans:
    print(*x[1])
