# ひとまず毎回ソートするバージョン
# Python 3, pypy ともにTLE

n, m = list(map(int, input().split() ))
values = list(map(int, input().split() ))

for i in range(m):
	max_card, num = list(map(int, input().split() ))

	values.sort()
	for j in range(max_card):
		if values[j] < num:
			values[j] = num
		else:
			break

print (sum(values))