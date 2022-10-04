# В списке все элементы попарно различны. Поменяйте местами
# минимальный и максимальный элемент этого списка.
List = list(map(int, input().split()))
a = List.index(min(List))
b = List.index(max(List))
List[a], List[b] = List[b], List[a]
print(*List)
