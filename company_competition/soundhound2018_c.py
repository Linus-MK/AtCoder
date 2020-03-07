# グリッドグラフ上の最大独立集合（=最大安定集合）のサイズを求める
# 一般のグラフ上で、独立集合の補集合は点カバーであるから、最大独立集合の補集合は最小点カバー (蟻本p.198)
# 二部グラフ上の最小点カバーの問題は最大マッチング問題に帰着できる

V = -1 #頂点数
MAX_V = 10000 #最大頂点数。ここでは仮
# G = [] * V #グラフの隣接リスト表現

# uとvを結ぶ辺をグラフに追加する
def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

# 増加パスをDFS（深さ優先探索）で探す
def dfs(v):
	global used
	global match
#	print(used)
#	print(v)
	used[v] = True
	for u in G[v]:
		w = match[u]
		if(w<0 or (not used[w] and dfs(w) ) ):
			match[v] = u
			match[u] = v
#			print(match)

			return True

	return False


# 二部グラフの最大マッチングを求める
def bipartite_matching():
	global used
	global match
	num_matching = 0
	# memset (match, -1, sizeof(match))
	match = [-1] * MAX_V

	for v in range(V):
		if match[v] < 0:
			# memset (used, 0, sizeof(used))
			used = [False] * MAX_V

			if (dfs(v)):
				num_matching += 1
#		print(match)

	return num_matching

r, c = map(int, input().split() )


V = r*c #頂点数
MAX_V = r*c #最大頂点数。
# G = [] * V #グラフの隣接リスト表現
G = [[] for _ in range(V)]
used = [False] * V #DFSで既に調べたかのフラグ
match = [-1] * MAX_V #マッチングのペア

vv = 0
grid = []
for i in range(r):
	grid.append(input())
	vv += grid[-1].count(".")

# (0-indexで)上からi番目左からj番目の要素を i*c + j とする

# 横方向の連結を隣接リスト表現に追加
for i in range(r):
	for j in range(c-1):
		if grid[i][j] == grid[i][j+1] == ".":
			add_edge(i*c+j, i*c+j+1)

# 縦方向の連結を隣接リスト表現に追加
for i in range(r-1):
	for j in range(c):
		if grid[i][j] == grid[i+1][j] == ".":
			add_edge(i*c+j, (i+1)*c+j)

num_matching = bipartite_matching()

# print(vv , num_matching)
# print(G)

print(vv - num_matching)
