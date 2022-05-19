# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
n = int(input())
sum_x = 0


def f(n):
    if n == 0:
        return 1
    else:
        return f(n - 1) * n


for x in range(1, n + 1):
    x = f(x)
    sum_x += x
print(sum_x)
