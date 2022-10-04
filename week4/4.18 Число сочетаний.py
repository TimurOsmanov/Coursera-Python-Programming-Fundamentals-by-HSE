# По данным целым числам n и k  (0≤k≤n) вычислите C из n по k.
#  Решение оформите в виде функции C(n, k).
# Для решения используйте рекуррентное соотношение:
# С из К по N = (C из K по N-1) + (C из K-1 по N-1)
# И равенства:
# С(n, 1)=n
# C(n, n)=1


def C(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k == n:
        return 1
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


n, k = int(input()), int(input())
print(C(n, k))
