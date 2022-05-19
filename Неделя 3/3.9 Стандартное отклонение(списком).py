import statistics
li, n = list(), -1
while n != 0:
    n = int(input())
    li.append(n)
li.pop(len(li)-1)
print(statistics.stdev(li))
