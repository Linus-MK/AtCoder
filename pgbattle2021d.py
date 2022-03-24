n, m = list(map(int, input().split()))
start_nums = list(map(int, input().split()))
reverse_machine = [[0, n]]
for _ in range(m):
    a, b = list(map(int, input().split()))
    reverse_machine.append([a-1, b])

# 深さ優先探索 DFS のための木を作る

reverse_machine.sort(key=lambda x: x[0], lambda x: x[1])
print(reverse_machine)

# ----
# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(500000+10)

# 木の深さ優先探索
def add_edge(u, v):
	G[u].append(v)

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


visited = [False] * m+1
mins = [None] * m+1
maxs = [None] * m+1

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

