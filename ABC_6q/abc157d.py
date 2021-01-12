# Union-Find
# 蟻本p.81

# nが頂点数、mが辺の本数
n, m, k = map(int, input().split())


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

edges = [list(map(int, input().split())) for _ in range(m)]
edges = [[b[0]-1, b[1]-1] for b in edges]  # 1-index -> 0-index

block = [list(map(int, input().split())) for _ in range(k)]
block = [[b[0]-1, b[1]-1] for b in block]  # 1-index -> 0-index

friend_deg = [0] * n
for b in range(m):
    friend_deg[edges[b][0]] += 1
    friend_deg[edges[b][1]] += 1
    unite(edges[b][0], edges[b][1])

block_list = [[] for _ in range(n)]
for b in range(k):
    block_list[block[b][0]].append(block[b][1])
    block_list[block[b][1]].append(block[b][0])

ans_list = [0] * n

for i in range(n):
    ans_list[i] = size[find_root(i)] - 1 - friend_deg[i] # 自分自身を除く
    # 連結成分の中のblock関係を除外したい。
    # blockの次数だけを見てもダメだね。
    # 同じ連結成分の各点に対して……だと、連結成分の要素数がNあるときにTLEする
    # ブロックの各関係に対して……だと間に合う
    for blocked in block_list[i]:
        if is_same(i, blocked):
            ans_list[i] -= 1

ans_list = map(str, ans_list)
print(' '.join(ans_list))
