# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(100000+10)

# 木の深さ優先探索
def add_edge(u, v, distance ):
	G[u].append([v, distance])
	G[v].append([u, distance])

def dfs(vertex, distance_from_start):
	global colors

	colors[vertex] = distance_from_start % 2

	for info in G[vertex]:
		v = info[0]
		if colors[v] >= 0: 
			#探索済み
			pass
		else:
			dfs(v, distance_from_start + info[1])

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

G = [[] for _ in range(n)] #グラフの隣接リスト表現
for edge in edges:
	add_edge(edge[0]-1, edge[1]-1, edge[2])

colors = [-1] * n
colors[0] = 0

dfs(0, 0)

for i in range(n):
	print(colors[i])
