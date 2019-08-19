s = input()
t = input()

len_s = len(s)
dp = [[-1 for _ in range(len_s)] for _ in range(26)]
# dp[i][j] = いまsのj文字目にいる。次に探しているのはアルファベットのi文字目であるとき、次までの必要文字数。
# print(len(dp))
# print(len(dp[0]))

for idx in range(len_s):

	ch = s[idx]
	i = ord(ch)-ord("a")
#	for j in range(len_s):
	if dp[i][0] == -1:
		dp[i] = [idx] * len_s
	else:
		temp = dp[i][idx]
		dp[i][temp+1:idx] = [idx] * (idx - temp + 1)

ans = 0
j = 0
first = True
for ch in t:

	i = ord(ch)-ord("a")

	if dp[i][j] < 0:
		print(-1)
		exit()

	distance = dp[i][j] - j
	if (not first )and distance <= 0 :
		distance += len_s
	ans += distance
	j = dp[i][j]

	first = False

print(ans + 1)
