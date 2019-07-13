#Greedy 貪欲法
n, capa, k = list(map(int, input().split()))
times = [int(input()) for _ in range(n)]
times.sort()

ans = 0
t_first_arrived = times[0]
num_first_arrived = 0

for i in range(n):
	if (times[i] > t_first_arrived + k):
		ans += 1
		t_first_arrived = times[i]
		num_first_arrived = i

	elif i >= num_first_arrived + capa:
		ans += 1
		t_first_arrived = times[i]
		num_first_arrived = i

ans += 1
print(ans)