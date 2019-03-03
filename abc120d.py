# union-findかな
# 蟻本によればunion-findは分割できないっぽいので、ちょっと違う? 
# 時刻を巻き戻して、橋なしから橋を建設することにすれば扱える

# 橋が崩落してA+B　がAとBに分かれたら、不便度はA*B増加する

n,m = map(int, input().split())

def find_root(x):
	if par[x] == x:
		return x
	else:
		par[x] = find_root(par[x])
		return par[x]

def unite(x, y):
	x = find_root(x)
	y = find_root(y)
	if(x == y):
		return 0

	if rank[x] < rank[y]:
		par[x] = y

		temp = size[x] * size[y]
		size[y] = size[x] + size[y] + 1
	else:
		par[y] = x
		if (rank[x] == rank[y]):
			rank[x] += 11

		temp = size[x] * size[y]
		size[x] = size[x] + size[y] + 1
	return temp



def is_same(x,y):
	return find_root(x) == find_root(y)

'''
par = list(n, 0)
rank = list(n, 0)
size = list(n, 1)
'''
par = [0]*n
rank = [0]*n
size = [1]*n

bridges = [list(map(int, input().split())) for _ in range(m)]
bridges = [[b[0]-1, b[1]-1] for b in bridges]

fuben_list = [0]*m
fuben = int(n * (n-1)/2)

for b in range(m-1,-1, -1):

	decr = unite(bridges[b][0] , bridges[b][1])
	fuben -= decr
	fuben_list[b] = fuben
	print(decr)

print(fuben_list)
