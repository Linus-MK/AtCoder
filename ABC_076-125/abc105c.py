import numpy as np
from functools import reduce

n = int(input())

X = 35
i = np.arange(X, dtype=np.int64)[::-1]
# 別法：i = np.flip(np.arange(X))

i = (-2)**i

ans = np.zeros(X, dtype=np.int64)

for digit in range(X):

	# 方針：
	# -2進数表記の一意性が問題中で言われているので、
	# 上位の桁から見ていって
	# 「注目してる桁より下位の反対符号の和を全部足しても届かなくなるならば、その桁は0で確定」とする
	sum_of_opposite = i[digit+1::2].sum() # 反対符号の和

	if i[digit] > 0 and i[digit] + sum_of_opposite > n:
		ans[digit] = 0
	elif i[digit] < 0 and i[digit] + sum_of_opposite < n:
		ans[digit] = 0
	else:
		ans[digit] = 1
		n -= i[digit]

# ansの先頭の0を削除して、桁をつなげる
print(int(reduce(lambda x, y: str(x) + str(y), ans)))
