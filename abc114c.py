'''
3^9 = 19683
3^10 = 59049
これくらいの数なら全探索して十分間に合う
'''

import itertools
from functools import reduce

n = int(input())
ketasuu = len(str(n))
ans = 0

base = itertools.product('357', repeat=ketasuu)
# baseはタプルからなるリスト

for i in base:
	if len(set(i))== 3: # 3種類の数字が1回以上使われている
		i_int = int(reduce(lambda x, y: x + y, i))
		if i_int <= n:
			ans += 1

for k in range(3, ketasuu):
	temp = 3**k - 3*1**k - 3 * (2**k - 2* 1**k)
	ans += temp

print(ans)
