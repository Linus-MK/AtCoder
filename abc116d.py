# Greedyを一ひねり
# 最初はGreedyに取る。それから種類を増やす。2個目以降を削除して、新たなネタの1個目を加える。
# あるネタの中でポイントが最高かどうかが重要。これを　True　/　False　で管理する
n, k = list(map(int, input().split()))

sushi = [list(map(int, input().split())) + [None] for _ in range(n)]
sushi.sort(key = lambda s: s[1] , reverse = True) #値段の降順

# あるネタの中でポイントが最高なら、 Trueそうでなければ、　False
neta_seen = set()
for i in range(n):
	if sushi[i][0] in neta_seen:
		sushi[i][2] = False
	else:
		sushi[i][2] = True
		neta_seen.add(sushi[i][0])

# n_kind = len([s[1] for s in sushi[:k] if s[1] == True ]) 
# なんかうまくいかないので、最初からk番目までのTrueの数を愚直に書こう
n_kind = 0
for i in range(k):
	if sushi[i][2]:
		n_kind += 1

ans = sum([s[1] for s in sushi[:k]]) + n_kind ** 2

now = ans
adopt = k
trash = k-1

while(True):

	while(adopt < n and sushi[adopt][2] == False):
		adopt += 1
	while(trash >= 0 and sushi[trash][2] == True):
		trash -= 1
	if not(adopt < n and trash >= 0):
		break

	now = now + sushi[adopt][1] - sushi[trash][1]
	now = now - n_kind**2 + (n_kind+1) ** 2

	n_kind += 1
	adopt += 1
	trash -= 1

	if now > ans:
		ans = now

print(ans)
