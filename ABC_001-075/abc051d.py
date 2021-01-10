# たぶん
# ある辺Eは、どの異なる2頂点間の、どの最短経路にも含まれない
# ⇔ ある辺Eは、その両端の2頂点間の、どの最短経路にも含まれない

# 証明：
# ⇒ は明らか
# ⇐ 背理法。任意の2頂点を取る。この頂点間の最短経路に、Eを通るものがあったとしよう。
# 仮定より、2頂点間の経路で、Eを使うよりも真に短いものが存在するので、
# 経路のうちEをそちらに置き換えたほうが真に短くなる。よって最短経路ではなく、矛盾。

# よって、「その両端の2頂点間の、どの最短経路にも含まれない」という辺の数を求めればよい。
# 全ての２頂点の組み合わせなのでワーシャルフロイド。それに最短経路自体を付け加えれば良い。

import copy

def warshall_floyd(distance, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    if 0 < edge_distance[i][j] < inf:
                        # 2回以上ここに当たる可能性があるか無いか分からないので、setで管理しちゃう。
                        # ついでに、i, jは両方入れて最後に２で割ればよい。
                        ans_set.add((i, j))
                        ans_set.add((j, i))

                    distance[i][j] = distance[i][k] + distance[k][j]


n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

inf = 10**10
distance = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    distance[i][i] = 0
ans_set = set()

for e in edges:
    e[0] -= 1  # 1-index → 0-index
    e[1] -= 1

    distance[e[0]][e[1]] = e[2]
    distance[e[1]][e[0]] = e[2]

edge_distance = copy.deepcopy(distance)  # 二重リストなので、普通のcopyだと不可。deeocopyにする

warshall_floyd(distance, n)

print(len(ans_set)//2)
# print(ans_set)