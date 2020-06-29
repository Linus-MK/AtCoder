# 木なので、任意の2点を結ぶルートはただ1つだけ存在する
# 最初にそこを順に埋めるのが最適。後は自分の陣営を埋めていく。
# 問題：点1→点Nのルートをどう求める? →幅優先探索かなぁ。

# 幅優先探索を2回やる必要がありそう
# 1回目で点1→点Nのルートを辿る。各点で1つ前の点をメモ。点Nから点1に逆にたどり、距離が半分の点Pを記録する
# 2回めでもう一度点1から辿る、点Pから先は探索しない（Snukeに取られる部分）。探索できた地点数が半分以上か否かを調べる

from collections import deque

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

neighbor = [[] for i in range(n)]
for e in edges:
    neighbor[e[0] - 1].append(e[1] - 1)
    neighbor[e[1] - 1].append(e[0] - 1)
    # 1-index → 0-index

info = [(-1, -1)] * n
info[0] = (0, -1) # 点1からの距離, 1つ点1寄りの点の番号

q = deque([])
q.append(0)

# 1回目
while True:
    v = q.popleft()
    distance = info[v][0]
    for nei in neighbor[v]:
        if info[nei][0] < 0:
            q.append(nei)
            info[nei] = (distance + 1, v)
    if len(q) == 0:
        break

# print(info)

# 点1〜点Nの距離が 10の場合、先手は5まで行ける。11の場合、5まで行ける。
# 逆に辿る
now = n-1
distance = info[n-1][0]
half = distance // 2

if distance == half + 1:
    # distance = 1の場合
    snuke_side_marginal = now
else:
    while True:
        now = info[now][1]
        distance -= 1
        if distance == half + 1:
            snuke_side_marginal = now
            break

# print(snuke_side_marginal)

info = [(-1, -1)] * n
info[0] = (0, -1) # 点1からの距離, 1つ点1寄りの点の番号

q = deque([])
q.append(0)

n_visited = 1
# 2回目

while True:
    v = q.popleft()
    distance = info[v][0]
    for nei in neighbor[v]:
        if info[nei][0] < 0 and nei != snuke_side_marginal:
            q.append(nei)
            info[nei] = (distance + 1, v)
            n_visited += 1

    if len(q) == 0:
        break

if n_visited > n - n_visited:
    print('Fennec')
else:
    print('Snuke')
