import numpy as np


rows,cols = list(map(int,input("请输入矩阵的行数: ").split()))



matrix = []


for i in range(rows):

    row_input = input(f"请输入第 {i+1} 行的 {cols} 个元素，并用空格分隔: ")

    row = list(map(int, row_input.split()))

    matrix.append(row)


matrix = np.array(matrix)

print("你输入的矩阵是:")
print(matrix)
