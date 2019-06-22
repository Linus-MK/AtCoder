# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(100000+10)

# 木の深さ優先探索
def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

def dfs(vertex, x_set, y_set):

	global visited

	if visited[vertex]:
		#探索済み
		return 0
	visited[vertex] = True

	x_set.add(coords[vertex][1])
	y_set.add(coords[vertex][2])
	for v in G[vertex]:
		if visited[v]:
			#探索済み
			pass
		else:
			dfs(v, x_set, y_set)

	return len(x_set)*len(y_set)

n = int(input())

G = [[] for _ in range(n)] #グラフの隣接リスト表現

visited = [False] * n
now_index = n-1

coords = [ [i] + list(map(int, input().split())) for i in range(n)]

from operator import itemgetter

# xでソート
coords_xs = sorted(coords, key = itemgetter(1))
for i in range(n-1):
	if coords_xs[i][1] == coords_xs[i+1][1]: 
		# 隣接 coords_xs[i][0] coords_xs[i+1][0]
		add_edge(coords_xs[i][0], coords_xs[i+1][0])

# yでソート
coords_ys = sorted (coords, key = itemgetter(2))
for i in range(n-1):
	if coords_ys[i][2] == coords_ys[i+1][2]: 
		# 隣接 coords_ys[i][0] coords_ys[i+1][0]
		add_edge(coords_ys[i][0], coords_ys[i+1][0])

# 深さ優先探索
final = 0
for i in range(n):
	x_set = {coords[i][1]} #set
	y_set = {coords[i][2]}
	final += dfs(i, x_set, y_set)

print(final - n)
# print(coords)
