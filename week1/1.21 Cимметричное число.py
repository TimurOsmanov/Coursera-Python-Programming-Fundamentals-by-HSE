a = int(input())
A = (a // 1000) # 1s numeral of number / первая цифра числа
B = (a // 100 % 10) #2nd numeral of number
C = (a // 10 % 10) #3rd numeral of number
D = (a % 1000 % 10) #4th numeral of number
print((A - D) ** 2 + (B - C) ** 2 + 1)
