# 幅優先探索, BFS
from collections import deque

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0]-1].append(edge[1]-1)  # 1- → 0-index
    neighbor[edge[1]-1].append(edge[0]-1)


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
    
    ans = max(ans, group_population)
        
print(ans)
