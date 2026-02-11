
class Matrix:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(lines)]


    def add(self, other_matrix):
        if self.lines != other_matrix.lines or self.columns != other_matrix.columns:
            raise ValueError("Разные размеры матриц!")

        result = Matrix(self.lines, self.columns)
        for i in range(self.lines):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
        return result

    def minus(self, other_matrix):
        if self.lines != other_matrix.lines or self.columns != other_matrix.columns:
            raise ValueError("Разные размеры матриц!")

        result = Matrix(self.lines, self.columns)
        for i in range(self.lines):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] - other_matrix.matrix[i][j]
        return result

    def multiply(self, other_matrix):
        if self.columns != other_matrix.lines:
            raise ValueError("Размер столбцов не равен размеру строк!")

        result = Matrix(self.lines, other_matrix.columns)
        for i in range(self.lines):
            for j in range(other_matrix.columns):
                num = 0
                for k in range(self.columns):
                    num += self.matrix[i][k] * other_matrix.matrix[k][j]
                result.matrix[i][j] = num
        return result

    def transpose(self):
        result = Matrix(self.columns, self.lines)
        for i in range(self.lines):
            for j in range(self.columns):
                result.matrix[j][i] = self.matrix[i][j]
        return result


def view(matrix):
    for i in matrix:
        for j in i:
            print(j, end="   ")
        print()


matrix_1 = Matrix(2, 3)
matrix_1.matrix = [[1, 2, 3], [4, 5, 6]]

matrix_2 = Matrix(2, 3)
matrix_2.matrix = [[7, 8, 9], [10, 11, 12]]

print("\nМатрица 1:")
view(matrix_1.matrix)

print("\nМатрица 2:")
view(matrix_2.matrix)

print("\nСложение матриц:")
new_matrix = matrix_1.add(matrix_2)
view(new_matrix.matrix)

print("\nВычетание матриц:")
view(matrix_1.minus(matrix_2).matrix)

matrix_3 = Matrix(3, 2)
matrix_3.matrix = [[1, 2], [3, 4], [5, 6]]

print("\nУмножение матриц:")
view(matrix_1.multiply(matrix_3).matrix)


print("\nТранспонирование матрицы 1:")
view(matrix_1.transpose().matrix)
