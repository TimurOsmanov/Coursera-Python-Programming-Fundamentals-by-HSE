from sys import stdin
# Добавьте в предыдущий класс следующие методы:
#
#  __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#
#  __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#
#  __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае,
#  аргумент находится справа. Для реализации этого метода в коде класса
#  достаточно написать __rmul__ = __mul__.


class Matrix:
    def __init__(self, my_li):
        self.my_li = list(map(lambda z: z.copy(), my_li))

    def __str__(self):
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), self.my_li))

    def size(self):
        return len(self.my_li), len(self.my_li[0])

    def __add__(self, other):
        ans, ans1 = [], []
        w = zip(self.my_li, other.my_li)
        for x in w:
            for i in range(len(x[0])):
                (lambda a, b: ans1.append(a[i] + b[i]))(*x)
            ans.append(ans1)
            ans1 = []
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), ans))

    def __mul__(self, other):
        result = map(lambda x: list(map(lambda z: z * other, x)), self.my_li)
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), result))

    __rmul__ = __mul__


exec(stdin.read())
