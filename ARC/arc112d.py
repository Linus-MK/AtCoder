# Union-Find
# 蟻本p.81

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

# 全マスに到達できる条件は、全部の行もしくは全部の列に到達できること。
# 列と行の到達可能関係をグラフにする。
# グラフの頂点として「各列および各行」を取る。
# 例えば第2行第3列に#があれば、2行目と3列目を互いに到達可能として結ぶ。すなわちUnion-Findである。
# 全部の#に対応する辺で結んだあと、到達可能な行列を求めて、行列のうち効率のいいものを採用すれば良い。
# 1つ以上結んだ集合（#が1個以上あることによって行列が結ばれた集合）の場合、それとつなぐことによって不利益にはならないので
# つなぐと決めつけて良い。
# 完全に孤立したグラフ頂点 = 「各列および各行」は、全列を目指すときは列の方だけ考え、全行を目指すときは行の方だけ考えれば良い。

# 行を0〜h-1,
# 列を10000〜10000+w-1で管理する。
# むりだわ。
# 列をh ~ w+h-1で管理する。

# nが頂点数、mが辺の本数
# n, m = map(int, input().split())

h, w = map(int, input().split())
n = h+w

par = list(range(n))  # 当該要素の親 最初は自分自身
# par = list(range(w)) + list(range(10000, 10000+h))  # 当該要素の親 最初は自分自身
# par = {}
# for x in range(w):
#     par[x] = x
# for x in range(10000, 10000+h):
#     par[x] = x

rank = [0]*n  # 木の深さ
size = [1]*n  # 集合の要素数 蟻本にはないけど、使うこともあるので入れとこう
# 注意：要素iの属する連結成分の要素数は、size[find_root(i)]である

# edges = [list(map(int, input().split())) for _ in range(m)]
# edges = [[b[0]-1, b[1]-1] for b in edges]  # 1-idx -> 0-idx

for row in range(h):
    masu = input()
    for col, cell in enumerate(masu):
        if cell == '#':
            unite(row, col+h)

unite(0, h+w-1)
unite(h-1, h+w-1)
unite(0, h)
unite(h-1, h)

cost_for_all_row = 0
cost_for_all_col = 0

for row in range(h):
    if is_same(row, 0):
        pass
    else:
        if size[row] > 1:
            # 行でも列でも併合するわ
            unite(row, 0)
            cost_for_all_col += 1
            cost_for_all_row += 1
        else:
            # 全行カバーの場合だけ併合するわ
            # uniteはしてもしなくても可
            cost_for_all_row += 1

for col in range(h, w+h):
    if is_same(col, 0):
        pass
    else:
        if size[col] > 1:
            # 行でも列でも併合するわ
            unite(col, 0)
            cost_for_all_col += 1
            cost_for_all_row += 1
        else:
            # 全列カバーの場合だけ併合するわ
            # uniteはしてもしなくても可
            cost_for_all_col += 1

print(min(cost_for_all_col, cost_for_all_row))
