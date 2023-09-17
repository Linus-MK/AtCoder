# Union-Find
# 蟻本p.81

# nが頂点数、mが辺の本数
n, m = map(int, input().split())


# 木の根を求める
def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]


# xとyの属する要素を併合
def unite(x_in, y_in):
    x = find_root(x_in)
    y = find_root(y_in)
    if(x == y):

        if color[x_in] == color[y_in]:
            # すでに同じ集合に属していて、なおかつ色が同色。
            # 操作終了。答えはこの辺の重さ
            return 1
        else:
            # すでに同じ集合に属していて、なおかつ色が異なる。何もしない
            return 0
    
    # 色を塗ります。
    # ここに来たときには同じグループでないことに注意
    # 2つとも無色の場合→適当に決める
    if color[x_in] < 0 and color[y_in] < 0:
        color[x_in] = 0
        color[y_in] = 1
    # 片方が無色の場合→もう片方はもう一方の色
    elif color[x_in] >= 0 and color[y_in] < 0:
        color[y_in] = 1 - color[x_in]
    elif color[x_in] < 0 and color[y_in] >= 0:
        color[x_in] = 1 - color[y_in]
    # 2つが異なる色の場合→何もしない
    # 2つが同じ色の場合→すべての色をひっくり返す
    elif color[x_in] == color[y_in]:
        # O(N)かかってる……
        base = find_root(x_in)
        for i in range(n):
            if find_root(i) == base:
                color[i] = 1 - color[i]

    if rank[x] < rank[y]:
        par[x] = y

        size[y] = size[x] + size[y]
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

        size[x] = size[x] + size[y]


# xとyが同じ集合に属するか否か
def is_same(x, y):
    return find_root(x) == find_root(y)


par = list(range(n))  # 当該要素の親 最初は自分自身
rank = [0]*n  # 木の深さ
size = [1]*n  # 集合の要素数 蟻本にはないけど、使うこともあるので入れとこう
color = [-1] * n # -1未決定、0赤、1青
# 注意：要素iの属する連結成分の要素数は、size[find_root(i)]である

edges = [list(map(int, input().split())) for _ in range(m)]
edges = [[b[0]-1, b[1]-1, b[2]] for b in edges]  # 1-idx -> 0-idx
edges.sort(key=lambda b: b[2])

for b in range(m):
    ret = unite(edges[b][0], edges[b][1])

    # print(color)

    if ret == 1:
        # 操作終了。答えはこの辺の重さ……とは限らない。
        # 例1では この辺の重さが12、2辺の合計最小が11なので答えは11。
        ans_1 = edges[b][2]
        break

# 無矛盾に全部の頂点を塗れた場合（これはグラフが2部グラフであることと同値）、答えは辺2つで行けるうちの最小である
# DFSやBFSを使わなくとも、各頂点に対して「そこから伸びる辺のうち最小2つの重さの和」を出せば良い。

ans = 10 ** 12

nei = [[] for _ in range(n)]
for b in range(m):
    nei[edges[b][0]].append(edges[b][2])
    nei[edges[b][1]].append(edges[b][2])

for i in range(n):
    t = nei[i]
    if len(t) >= 2:
        t2 = sorted(t)
        ans = min(ans, t2[0]+t2[1])

ans = min(ans_1, ans)

print(ans)
