from collections import deque

def bfs_min_moves(ice_rink, start, end, n, m):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x, y
            
            # 滑向当前方向，直到撞到障碍物或边界
            while 0 <= nx + dx < n and 0 <= ny + dy < m and ice_rink[nx + dx][ny + dy] != '#':
                nx += dx
                ny += dy
                
            if (nx, ny) == end:
                return moves + 1
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
    
    return -1

# 读取输入
n, m = map(int, input().split())
ice_rink = [input().strip() for _ in range(n)]

start = end = None
for i in range(n):
    for j in range(m):
        if ice_rink[i][j] == 'S':
            start = (i, j)
        elif ice_rink[i][j] == 'E':
            end = (i, j)

# 找到最少的步数
result = bfs_min_moves(ice_rink, start, end, n, m)
print(result)
