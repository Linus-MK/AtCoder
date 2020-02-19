k, x =  list(map(int, input().split() ))
# 場合分け不要

a = range(x-k+1, x+k-1 + 1)
a = list(a)
a = map(str, a)
print(" ".join(a))
# for i in range(x-k+1, x+k-1 + 1):
# 	print(i)