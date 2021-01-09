# ABC078 Dからコピペして修正したけど、バグってWAになった。

n = int(input())
edges = [list(map(int, input().split())) for i in range(n)] 

# 辺を通って到達可能か否かで分かれる。→幅優先か深さ優先かUnion-Findだな。
# 迷ったら幅優先で書こう。

# 閉路があるか無いかの判定：visitedが発生するかどうか

from collections import deque

vertex_num = 400000
nei = [[] for _ in range(vertex_num)]
for edge in edges:
    v0 = edge[0] - 1
    v1 = edge[1] - 1
    nei[v0].append(v1)
    nei[v1].append(v0)

queue = deque()
visited = [False] * vertex_num
prev = [-1] * vertex_num

ans = 0
for i in range(vertex_num):
    if visited[i]:
        continue
    queue.append(i)
    # ans += 1

    contain_loop = False
    while len(queue) > 0:
        v = queue.popleft()
        if visited[v]:
            # この独立成分は閉路を含む
            contain_loop = True
            # pass
        else:
            visited[v] = True
            ans += 1

            for nextt in nei[v]:
                queue.append(nextt)
                prev = 
    
    if not contain_loop:
        ans -= 1

print(ans)
