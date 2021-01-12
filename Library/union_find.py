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
def unite(x, y):
    x = find_root(x)
    y = find_root(y)
    if(x == y):
        return 0

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
# 注意：要素iの属する連結成分の要素数は、size[find_root(i)]である

edges = [list(map(int, input().split())) for _ in range(m)]
edges = [[b[0]-1, b[1]-1] for b in edges]  # 1-idx -> 0-idx

for b in range(m):
    unite(edges[b][0], edges[b][1])
