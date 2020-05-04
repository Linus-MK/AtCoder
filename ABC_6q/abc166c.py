# nが頂点数、mが辺の本数
n, m = map(int, input().split())

heights = list(map(int, input().split())) 

edges = [list(map(int, input().split())) for _ in range(m)]
edges = [[b[0]-1, b[1]-1] for b in edges]  # 1-idx -> 0-idx

neighbor = [[] for i in range(n)]
# print(neighbor)
for i in range(m):
    a = edges[i][0]
    b = edges[i][1]
    neighbor[a] += [b]
    neighbor[b] += [a]
# print(neighbor)


ans = 0
for vertex in range(n):
    result = True
    for nei in neighbor[vertex]:
        if heights[nei] >= heights[vertex]:
            result = False
        
    if result:
        ans += 1
            
print(ans)
