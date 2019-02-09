'''
3^9 = 19683
3^10 = 59049
これくらいの数なら全探索して十分間に合う
'''

import itertools
from functools import reduce

n = int(input())
ans = 0

for length in range(3, len(str(n)) +1):
	base = itertools.product('357', repeat=length)
	# baseはタプルからなるリスト
	for i in base:
		if len(set(i))== 3: # 3種類の数字が1回以上使われている
			i_int = int(reduce(lambda x, y: x + y, i))
			if i_int <= n:
				ans += 1

print(ans)
