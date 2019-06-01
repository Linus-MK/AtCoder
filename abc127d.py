# ひとまず毎回ソートするバージョン
# Python 3, pypy ともにTLE
import bisect

n, m = list(map(int, input().split() ))
values = list(map(int, input().split() ))
values.sort()

for i in range(m):
	max_card, num = list(map(int, input().split() ))

	num_small = bisect.bisect(values, num)
	num_to_change = min(max_card, num_small)

	# sort
	# values = values[num_to_change:num_small] + [num]*num_to_change + values[num_small:]
	del  values[:num_to_change]
	values[num_small - num_to_change : num_small - num_to_change] = [num]*num_to_change

print (sum(values))