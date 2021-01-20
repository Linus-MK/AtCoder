# 幅優先探索
# ほかからコピペせずにまっさらから幅優先探索を書いたから大丈夫かな……

import collections

n, m = list(map(int, input().split()))
# 最初nを人間、次のmを言語
neighbor = [[] for _ in range(n+m)]
visited = [False] * (n+m)
for i in range(n):
    line = list(map(int, input().split()))
    for lang in line[1:]:
        neighbor[i].append(n+lang-1)
        neighbor[n+lang-1].append(i)

queue = collections.deque()

# 適当な人間から探索を始める
queue.append(0)

while len(queue) > 0:
    vertex = queue.popleft()
    visited[vertex] = True

    nei = neighbor[vertex]
    for v in nei:
        if not visited[v]:
            queue.append(v)
            # これ、同じ頂点が複数回appendされて複数回popleftされるけど、計算量大丈夫なのか?
            # なんでこれでTLEじゃなくてACになったの???

ans = 'YES'
for i in range(n):
    if not visited[i]:
        ans = 'NO'
print(ans)
