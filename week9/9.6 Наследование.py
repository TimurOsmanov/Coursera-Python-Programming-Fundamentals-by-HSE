from sys import stdin
import itertools


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, my_li):
        self.my_li = list(map(lambda z: z.copy(), my_li))

    def __str__(self):
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), self.my_li))

    def size(self):
        return len(self.my_li), len(self.my_li[0])

    def __add__(self, other):
        if self.size() == other.size():
            ans, ans1 = [], []
            w = zip(self.my_li, other.my_li)
            for x in w:
                for i in range(len(x[0])):
                    (lambda a, b: ans1.append(a[i] + b[i]))(*x)
                ans.append(ans1)
                ans1 = []
            return Matrix(ans)
        else:
            error = MatrixError(self, other)
            raise error

    def __mul__(self, other):
        result = []
        if isinstance(other, int) or isinstance(other, float):
            result = map(lambda t: list(map(lambda p: p * other, t)), self.my_li)
        elif isinstance(other, Matrix):
            if self.size()[1] == other.size()[0]:
                temp_ans, ans_line, mul_combinations = [], [], []
                temp_sum = 0
                for x in self.my_li:
                    mul_combinations.append(zip(itertools.repeat(x), other.transposed().my_li))
                for z in mul_combinations:
                    for c in z:
                        for i in range(len(c[0])):
                            (lambda a, b: temp_ans.append(a[i] * b[i]))(*c)
                        for q in temp_ans:
                            temp_sum += q
                        ans_line.append(temp_sum)
                        temp_sum = 0
                        temp_ans = []
                    result.append(ans_line)
                    ans_line = []
            else:
                error = MatrixError(self, other)
                raise error
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        n, ans, ans1 = 0, [], []
        for x in self.my_li:
            if n == 0:
                for i in range(len(x)):
                    ans1.append(x[i])
                    ans.append(ans1)
                    ans1 = []
                n += 1
            else:
                for z in self.my_li[1:]:
                    for i in range(len(ans)):
                        ans[i].append(z[i])
                break
        self.my_li = ans
        return Matrix(self.my_li)

    def transposed(self):
        temp = list(map(lambda z: z.copy(), self.my_li))
        return Matrix(temp).transpose()


class SquareMatrix(Matrix):
    def __mul__(self, x):
        return SquareMatrix(super().__mul__(x).my_li)

    def __pow__(self, power):
        if power in [0, 1]:
            return self
        elif power == 2:
            return self * self
        if power % 2 != 0:
            return self * (self**(power - 1))
        else:
            return (self * self)**(power // 2)


exec(stdin.read())
