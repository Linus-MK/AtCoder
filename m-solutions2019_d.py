# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(100000+10)

# 木の深さ優先探索
def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

def dfs(vertex):
	global values
	global now_index

	values[vertex] = values_to_give[now_index]
	now_index -= 1

	for info in G[vertex]:
		v = info
		if values[v] >= 0: 
			#探索済み
			pass
		else:
			dfs(v)

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
values_to_give = list(map(int, input().split()))
values_to_give.sort()

G = [[] for _ in range(n)] #グラフの隣接リスト表現
for edge in edges:
	add_edge(edge[0]-1, edge[1]-1)

values = [-1] * n
# values[0] = values_to_give[n-1]
now_index = n-1

dfs(0)

mmm = list(map(str, values))
print(sum(values_to_give) - max(values_to_give))
print(" ".join(mmm))
