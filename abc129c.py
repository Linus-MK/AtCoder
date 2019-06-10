n, m = list(map(int, input().split() ))
broken = [int(input()) for _ in range(m)]
broken.append(-1) #番兵
broken_idx = 0

mod = 10**9+7

num_way = [0] * (n+1)
num_way[0] = 1
if broken[broken_idx] == 1:
	num_way[1] = 0
	broken_idx += 1
else:
	num_way[1] = 1

for i in range(2, (n+1)):
	if broken[broken_idx] == i:
		num_way[i] = 0
		broken_idx += 1
	else:
		num_way[i] = (num_way[i-1] + num_way[i-2]) % mod

print (num_way[n])