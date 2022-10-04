# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².
i = int(input())
sum_n = 0
for n in range(0, i + 1):
    n = n**2
    sum_n += n
print(sum_n)
