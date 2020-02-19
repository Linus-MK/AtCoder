n, k = list(map(int, input().split() ))

prob_sum = 0

for i in range(1 , n+1):
	now = i
	prob = 1.0

	while now < k:
		now *= 2
		prob /= 2
	prob_sum += prob
print(prob_sum / n)
