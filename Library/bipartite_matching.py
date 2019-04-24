# 二部グラフに対する最大マッチング
# 二部グラフの最大独立集合（=最大安定集合）、最小点カバーの問題は最大マッチング問題に帰着できる(蟻本p.198)

# 蟻本p.196をpythonに移植

V = -1 #頂点数
MAX_V = 10000 #最大頂点数
G[MAX_V] = [] #グラフの隣接リスト表現
match[MAX_V] = [] #マッチングのペア
used[MAX_V] = [] #DFSで既に調べたかのフラグ


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

