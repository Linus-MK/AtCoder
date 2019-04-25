# 二部グラフに対する最大マッチング
# 二部グラフの最大独立集合（=最大安定集合）、最小点カバーの問題は最大マッチング問題に帰着できる(蟻本p.198)

# 蟻本p.197をpythonに移植

V = -1 #頂点数
MAX_V = 10000 #最大頂点数。ここでは仮
G[MAX_V] = [] #グラフの隣接リスト表現
match[MAX_V] = [] #マッチングのペア
used[MAX_V] = [] #DFSで既に調べたかのフラグ

# uとvを結ぶ辺をグラフに追加する
def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

# 増加パスをDFS（深さ優先探索）で探す
def dfs(v):
	used[v] = True
	for u in G[v]:
		w = match[u]
		if(w<0 or (!used[w] and dfs(w) ) ):
			match[v] = u
			match[u] = v
			return True

	return False


# 二部グラフの最大マッチングを求める
def bipartite_matching():
	num_matching = 0
	# memset (match, -1, sizeof(match))
	match = [-1] * MAX_V

	for v in range(V):
		if match[v] < 0:
			# memset (used, 0, sizeof(used))
			used = [0] * MAX_V

			if (dfs(v)):
				num_matching += 1

	return num_matching

