# 矩阵计算

## 概述
本项目实现了一个简单的矩阵计算工具，通过定义一个 `MatrixCalculate` 类来支持基本的矩阵操作，包括加法、乘法和转置。此外，还提供了用户界面以方便输入矩阵数据，并能够输出计算结果。

## 功能特性
- **加法**：两个相同大小的矩阵可以进行加法运算
- **乘法**：当第一个矩阵的列数与第二个矩阵的行数相等时，可以进行矩阵乘法运算
- **转置**：可以计算任意矩阵的转置矩阵
- **输入**：允许用户手动输入矩阵数据
- **输出**：能够清晰地显示矩阵运算的结果

## 使用方法
1. 运行程序后，根据提示输入第一个矩阵的行数及元素
2. 同样地，输入第二个矩阵的数据
3. 程序会自动计算并显示两个矩阵的加法和乘法结果（如果适用），以及各自的转置矩阵

>代码如下：
```python
import numpy as np
# 矩阵类
class MatrixCalculate:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    #加法
    def add(self, matrix_2):
        if self.rows != matrix_2.rows or self.cols != matrix_2.cols:
            raise ValueError("行列数不相等")
        return MatrixCalculate(self.matrix + matrix_2.matrix)

    #乘法
    def multiply(self, matrix_2):
        if self.cols != matrix_2.rows:
            raise ValueError("第一个矩阵的列数和第二个矩阵的行数不相等")
        return MatrixCalculate(np.dot(self.matrix, matrix_2.matrix))
    
    #转置
    def transpose(self):
        return MatrixCalculate(self.matrix.T)


#输入矩阵
def input_matrix(x):
    print(x)
    rows = int(input("输入行数: "))
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return MatrixCalculate(matrix)

#打印函数
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

#主函数
def main():
    m1 = input_matrix("输入第一个矩阵:")
    m2 = input_matrix("输入第二个矩阵:")

    print("\n加法:")
    try:
        print_matrix(m1.add(m2).matrix)
    except ValueError as e:
        print(f"加法错误: {e}")

    print("\n乘法:")

    try:
        print_matrix(m1.multiply(m2).matrix)
    except ValueError as e:
        print(f"乘法错误: {e}")

    print("\n转置1:")
    print_matrix(m1.transpose().matrix)

    print("\n转置2:")
    print_matrix(m2.transpose().matrix)

main()
```