n, dim = list(map(int, input().split()))

coodi = []
count = 0
for i in range(n):
	coodi.append( list(map(int, input().split())) )

for i in range(n):
	for j in range(i+1, n):
		dist = 0
		for d in range(dim):
			dist += ( coodi[i][d] - coodi[j][d] ) ** 2
		for k in range(0, 200):
			if k ** 2 == dist:
				count += 1
				break

print(count)