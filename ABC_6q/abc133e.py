# 久々の幅優先探索……

import queue

n, k = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

def add_edge(u, v ):
	G[u].append(v)
	G[v].append(u)

G = [[] for _ in range(n)] #グラフの隣接リスト表現
for edge in edges:
	add_edge(edge[0]-1, edge[1]-1)

q = queue.Queue()
q.put(0)

n_colors = [-1] * n
n_colors[0] = k

count = 0
for v in G[0]:
	q.put(v)
	n_colors[v] = k - count - 1 #※
	count += 1

while(q.qsize() > 0):
	now = q.get()
	count = 0
	for v in G[now]:
		if n_colors[v] >= 0:
			pass
		else:
			q.put(v)
			n_colors[v] = k - count - 2
			count += 1

			if n_colors[v] == 0:
				print(0)
				exit()

ans = 1
for i in range(n):
	ans *= n_colors[i]
	ans %= (10 ** 9 + 7)

print(ans)
