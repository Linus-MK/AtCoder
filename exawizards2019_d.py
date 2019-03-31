N,X =  map(int, input().split())
s = list(map(int, input().split()))
 
import math
import copy
 
modu = 1000000007
 
def get_residue_sum(a, li, length):
	if a < min(li):
		# 残り全部n
		return a * math.factorial(length)
	elif length == 1:
		return a % li[0]
	else:
		summ = 0
		for idx in range(length):
#			li から iを削除して
			li2 = copy.deepcopy(li)
			q = li2.pop(idx)
			summ += get_residue_sum(a%q, li2, length-1)
		return (summ % modu)
 
ans = get_residue_sum(X, s, N) % modu
print(ans)
