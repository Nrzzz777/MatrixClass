class Matrix:
    def __init__(self, elements):
        self.elements = elements
        self.rows = len(elements)
        self.cols = len(elements[0]) if self.rows > 0 else 0
    
    def __add__(self, other):
        if not isinstance(other, Matrix) or (self.rows != other.rows or self.cols != other.cols):
            raise ValueError("Matrices must have the same dimensions to be added.")
        result = [[self.elements[i][j] + other.elements[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix) or (self.rows != other.rows or self.cols != other.cols):
            raise ValueError("Matrices must have the same dimensions to be subtracted.")
        result = [[self.elements[i][j] - other.elements[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix) or self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = [[sum(self.elements[i][k] * other.elements[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.elements])

# 示例代码
if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("m1 + m2:")
    print(m1 + m2)
    print("m1 - m2:")
    print(m1 - m2)
    print("m1 * m2:")
    print(m1 * m2)