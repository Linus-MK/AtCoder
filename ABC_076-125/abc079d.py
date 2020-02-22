# 壁の各マスは独立に扱ってよいので、2→1、3→1、……の最低コストを求めればよい。
# https://qiita.com/e869120/items/eb50fdaece12be418faa だとワーシャル・フロイドの項に挙がっているが、
# ダイクストラだとダメなのかな?
# →ダイクストラは「ある1つの始点から、他のすべての点までの最短距離」をO(E log V)で計算する。
# 今回は始点が 1以外の9点なので、ダイクストラには向かない
# （2→3と3→2のコストは同じではないので、1から他のすべての点までを計算するのは不可。
# ダイクストラでも計算コスト上はできる。ダイクストラを9回やる羽目になるけど。）


def warshall_floyd(distance, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


v = 10
h, w = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(10)]
wall = [list(map(int, input().split())) for i in range(h)]

warshall_floyd(d, v)

ans = 0
for i in range(h):
    for j in range(w):
        num = wall[i][j]
        if num == -1:
            pass
        else:
            # num → 1 の距離はc_{num, 1}
            ans += d[num][1]

print(ans)
