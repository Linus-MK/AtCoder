# グラフが連結とは限らない
# 連結成分の和が前後で等しいか
# 幅優先探索 BFS

n, m = list(map(int, input().split()))
begin = list(map(int, input().split()))
end = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0]-1].append(edge[1]-1)  # 1- → 0-index
    neighbor[edge[1]-1].append(edge[0]-1)

from collections import deque

visited = [-1] * n
ans = 1
for idx in range(n):
    if visited[idx] == -1:
        queue = deque()
        queue.append(idx)
        begin_val = begin[idx]
        end_val = end[idx]

        visited[idx] = 0
        while len(queue) > 0:
            vertex = queue.popleft()
            for nei in neighbor[vertex]:
                if visited[nei] == -1:
                    visited[nei] = 0
                    queue.append(nei)
                    begin_val += begin[nei]
                    end_val += end[nei]
    
    if begin_val != end_val:
        print('No')
        exit()
        
print('Yes')

