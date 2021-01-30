# 巡回セールスマン問題 → bitDP
# N頂点M辺のグラフで指定したK個の頂点を訪問するための移動距離と読み替えると、巡回セールスマン問題ですねBitDPですねと分かる。
# K点間の距離行列を求めるのが一苦労で、各点から幅優先探索かダイクストラだろう。
# 蟻本のTSP実装が添字降順（デクリメント）で頭が混乱した。昇順で実装して正解した。

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
must_stone = list(map(int, input().split()))
must_stone = [s-1 for s in must_stone]  # 1- → 0-index

if k == 1:
    print(1)
    exit()
if m == 0:
    print(-1)
    exit()

# まず、k点の間の距離を距離行列にする必要がある。
# どうやって？
# k点のそれぞれの2点間の最短距離、枝長はすべて1
# ・k点から幅優先探索 O(k (E+V))
# ・k点からdijkstra法 O(k E log V)
# ABC068Cからコピペ

from collections import deque
neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0]-1].append(edge[1]-1)  # 1- → 0-index
    neighbor[edge[1]-1].append(edge[0]-1)


distance_mat = [[0 for _ in range(k)] for _ in range(k)]

for i in range(k):
    inf = 10 ** 8
    distance = [inf] * n
    
    queue = deque()
    stone_idx = must_stone[i]
    queue.append(stone_idx)
    distance[stone_idx] = 0
    while len(queue) > 0:
        vertex = queue.popleft()
        for nei in neighbor[vertex]:
            if distance[nei] == inf:
                distance[nei] = distance[vertex] + 1
                queue.append(nei)
    
    for j in range(k):
        stone_j = must_stone[j]
        distance_mat[i][j] = distance[stone_j]
    

# print(distance_mat)

# あとはこの距離行列を使って巡回セールスマン問題、bitDP

dp = [[inf for _ in range(k)] for _ in range(1<<k)]
# 初期値 1つ目の頂点はコスト1でいける（1個目の石！）
for i in range(k):
    dp[1<<i][i] = 1

for set_idx in range(1<<k):
    for current in range(k):
        if (set_idx & (1 << current)):
            for next_ in range(k):
                dp[set_idx | 1<<next_][next_] = min(
                    dp[set_idx | 1<<next_][next_], dp[set_idx][current] + distance_mat[current][next_])

ans = min(dp[(1<<k)-1])
if ans == inf:
    print(-1)
else:
    print(ans)
