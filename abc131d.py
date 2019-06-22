from operator import itemgetter
n = int(input())
tasks = [list(map(int, input().split() )) for _ in range(n)]
tasks.sort(key = itemgetter(1))
# 締切時刻をkeyとしてソート

t = 0
for i in range(n):
	t += tasks[i][0]
	if t > tasks[i][1]:
		print("No")
		exit()

print("Yes")
