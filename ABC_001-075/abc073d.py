# Rの制約条件が明らかに小さい。 回り方を全部試しても 8! = 40320通りである。
# 回り方を1個固定したらどの計算量で解ける?
# R個の点に対して、2点間の距離が必要なので、始点が複数ある。ワーシャルフロイドを使う。

def warshall_floyd(distance, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

n, m, r = list(map(int, input().split()))
destination = list(map(int, input().split()))
destination = [x-1 for x in destination]  # 1-index → 0-index

infinity = 10*5*200*2 
distance = [[infinity for _ in range(n)] for _ in range(n)]
for i in range(n):
    distance[i][i] = 0

for i in range(m):
    a, b, c = list(map(int, input().split()))
    distance[a-1][b-1] = c
    distance[b-1][a-1] = c

warshall_floyd(distance, n)

import itertools
ans = 10*10
for perm in itertools.permutations(range(r)):
    d = 0
    for i in range(r-1):
        start = destination[perm[i]]
        end = destination[perm[i+1]]
        d += distance[start][end]
    ans = min(ans, d)

print(ans)
