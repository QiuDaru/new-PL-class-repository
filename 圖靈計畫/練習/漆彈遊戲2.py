import numpy as np



n, m = list(map(int, input().split()))
matrix = np.full((n, n), 0)



ans = []




def Calculate_size(matrix, l, x, y, i, n):
    if (l - 1) // 2 > 1:
        l = (l - 1) // 2  
        

    matrix[x, y] = i

    n = (n - 1) // 2

    
    
    for z in range(n + 1):
        matrix[x + z, y] = i
        matrix[x - z, y] = i
        matrix[x, y + z] = i
        matrix[x, y - z] = i

        for z1 in range(1, n + 1):
            matrix[x + z1, y] = i
            matrix[x - z1, y] = i
            matrix[x, y + z1] = i
            matrix[x, y - z1] = i

            try:
                for z1 in range(l - 1):  
                    positions = [
                        (x + z, y + z1), (x - z, y + z1),
                        (x + z1, y + z), (x + z1, y - z),
                        (x + z, y - z1), (x - z, y - z1),
                        (x - z1, y + z), (x - z1, y - z),
                        (x + z1, y + z + z1), (x + z1, y + z - z1), 
                        (x + z1 + z, y + z1), (x - z1 + z, y + z1),
                        (x + z1, y + z + z1 + 1), (x + z + z1 + 1, y + z1),
                        (x + z1, y + z + z1), (x + z + z1, y + z1)
                    ]

                    for pos in positions:
                        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < matrix.shape[0] and pos[1] < matrix.shape[1]:  # 检查pos是否在矩阵边界内
                            matrix[pos] = i
                        else:
                            pass

            except Exception as e:
                print(f"错误: {e}")

    return matrix



def inquire(p, a, b, c, d,matrix):
    quantity = 0
    x_x = 0
    y_y = 0
    x_x = abs(a-c)
    y_y = abs(b-d)

    for y in range(y_y+1):
        for x in range(x_x+1):
            if matrix[a+x-1,b+y-1] == p:
                quantity += 1
    
    return quantity








for i in range(1, m+1):
    l, x, y = list(map(int, input("玩家操作: ").split()))
    x = x - 1
    y = y - 1
    matrix = Calculate_size(matrix, l, x, y, i, n)
    

    p, a, b, c, d = list(map(int, input("查詢: ").split()))
    
    ans.append(inquire(p, a, b, c, d, matrix))
for i in ans:
    print(i)
