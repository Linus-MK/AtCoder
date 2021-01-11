# 幅優先探索, BFS
from collections import deque

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0]-1].append(edge[1]-1)  # 1- → 0-index
    neighbor[edge[1]-1].append(edge[0]-1)

inf = 10 ** 8
distance = [inf] * n
ans = 1

queue = deque()
queue.append(0)
distance[0] = 0
while len(queue) > 0:
    vertex = queue.popleft()
    for nei in neighbor[vertex]:
        if distance[nei] == inf:
            distance[nei] = distance[vertex] + 1
            queue.append(nei)

if distance[n-1] <= 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
