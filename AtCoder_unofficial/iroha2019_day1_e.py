n, a, b = list(map(int, input().split()))

d = list(map(int, input().split()))
d.append(0)
d.append(n+1)
d.sort()

num_dating = 0
for i in range(1,len(d)):
	num_dating += (d[i] - d[i-1] - 1) // a #間
print(n - num_dating - b)
