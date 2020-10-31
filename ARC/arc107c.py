# 不変量を考えるやつ
# 操作によって各行各列の値の和は不変

# swap可能な行同士を線で結んで、連結成分の要素数の階乗の積

# ABC177 D 
import math
from collections import deque

n, max_sum = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for i in range(n)]
mod = 998244353

# 行方向
neighbor = [[] for _ in range(n)]
for row_i in range(n):
    for row_j in range(row_i+1, n):
        valid = True
        for idx in range(n):
            if matrix[row_i][idx] + matrix[row_j][idx] > max_sum:
                # だめ
                valid = False
                break
        if valid:
            neighbor[row_i].append(row_j)
            neighbor[row_j].append(row_i)

visited = [-1] * n
ans = 1
for idx in range(n):
    if visited[idx] == -1:
        queue = deque()
        queue.append(idx)
        group_population = 1
        visited[idx] = 0
        while len(queue) > 0:
            vertex = queue.popleft()
            for nei in neighbor[vertex]:
                if visited[nei] == -1:
                    visited[nei] = 0
                    queue.append(nei)
                    group_population += 1
    
        ans *= math.factorial(group_population)
        ans %= mod

# 列方向
neighbor = [[] for _ in range(n)]
for col_i in range(n):
    for col_j in range(col_i+1, n):
        valid = True
        for idx in range(n):
            if matrix[idx][col_i] + matrix[idx][col_j] > max_sum:
                # だめ
                valid = False
                break
        if valid:
            neighbor[col_i].append(col_j)
            neighbor[col_j].append(col_i)

visited = [-1] * n
# ans = 1
for idx in range(n):
    if visited[idx] == -1:
        queue = deque()
        queue.append(idx)
        group_population = 1
        visited[idx] = 0
        while len(queue) > 0:
            vertex = queue.popleft()
            for nei in neighbor[vertex]:
                if visited[nei] == -1:
                    visited[nei] = 0
                    queue.append(nei)
                    group_population += 1
    
        ans *= math.factorial(group_population)
        ans %= mod

print(ans)
