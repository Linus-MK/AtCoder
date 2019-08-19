# ★頂点1からdfsを始めればよいので、 自分の親はどれで子はどれなのか分からなくてもできる！

# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(200000+10)

# 木の深さ優先探索
def add_edge(u, v):
	G[u].append(v)
	G[v].append(u)

def dfs(vertex):
	global counters
	global visited

	visited[vertex] = True


	for v in G[vertex]:
		if visited[v]: 
			#探索済み
			pass
		else:
			# 子のに自分の値を足す
			counters[v] += counters[vertex]
			dfs(v)


n, n_query =  list(map(int, input().split() ))

edges = [list(map(int, input().split())) for _ in range(n-1)]
visited = [False] * n
counters = [0] * n

G = [[] for _ in range(n)] #グラフの隣接リスト表現
for edge in edges:
	add_edge(edge[0]-1, edge[1]-1)

# for i in range(n_query):
# 	p, x =  list(map(int, input().split() ))
# 	counters[p-1] += x

px = [list(map(int, input().split() )) for _ in range(n_query)]
for z in px:
	counters[z[0]-1] += z[1]

dfs(0)

#for i in range(n):
#	print(counters[i], end=" ")

x = map(str, counters)
print (" ".join(x))
