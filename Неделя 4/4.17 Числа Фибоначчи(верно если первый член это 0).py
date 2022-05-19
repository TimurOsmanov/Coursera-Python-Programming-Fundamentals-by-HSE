# Напишите функцию phib(n), которая по данному целому
# неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы - используйте рекурсию.
n = int(input())
i = 0
fib1 = 0
fib2 = 1


def phib(n):
    global fib1
    global fib2
    global i
    fibsum = fib1 + fib2
    if i != n - 1:
        i += 1
        fib1 = fib2
        fib2 = fibsum
        return phib(n)
    else:
        return fib1


print(phib(n))
