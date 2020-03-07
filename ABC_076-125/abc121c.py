n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

arr.sort(key = lambda x: x[0])
# ここは単にarr.sort()でもよい。
# この場合、x[0]を基準に大小比較し、x[0]が同一ならばx[1]を基準に大小比較する。
# 問題の性質より、x[0]が同一ならば入れ替えてもよい。
# https://docs.python.org/ja/3/tutorial/datastructures.html#comparing-sequences-and-other-types

honsuu = 0
price = 0
for i in arr:
	temp = min(i[1], m-honsuu)
	honsuu += temp
	price += i[0] * temp

print(price)
