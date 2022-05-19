from sys import stdin
# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
#
# В класс Matrix внесите следующие изменения:
#
#  Добавьте в метод __add__ проверку на ошибки в размере входных данных,
#  чтобы при попытке сложить матрицы разных размеров было выброшено исключение
#  MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
#  аргументом __add__ (просто self), а matrix2  —  вторым (второй операнд для сложения).
#
#  Реализуйте метод transpose, транспонирующий матрицу и возвращающую
#  результат (данный метод модифицирует экземпляр класса Matrix)
#
#  Реализуйте статический метод transposed, принимающий Matrix и
#  возвращающий транспонированную матрицу. Пример статического метода.


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
            return '\n'.join(map(lambda l: '\t'.join(map(str, l)), ans))
        else:
            error = MatrixError(self, other)
            raise error

    def __mul__(self, other):
        result = map(lambda x: list(map(lambda z: z * other, x)), self.my_li)
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), result))

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


exec(stdin.read())
