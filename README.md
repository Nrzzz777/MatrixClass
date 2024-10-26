# Matrix Class

这是一个简单的矩阵类实现，支持基本的数学运算：加法、减法和乘法。

## 特性

- 支持矩阵的加法、减法和乘法操作。
- 内置了错误检查机制，确保运算前后的矩阵维度正确。

## 使用方法

首先，确保你的环境中已经安装了 Python。

### 安装

无需额外安装依赖包，直接运行即可。

### 示例

```python
from matrix import Matrix

# 创建两个矩阵
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# 执行运算
print("m1 + m2:")
print(m1 + m2)
print("m1 - m2:")
print(m1 - m2)
print("m1 * m2:")
print(m1 * m2)