n = int(input())
a = list(map(int, input().split() ))

# どちらも同じ結果となる：
negative_values = list(filter(lambda x:x<0 , a) )
# negative_values = [x for x in a if x<0]
num_negative = len(negative_values)

if num_negative % 2 == 0 :
	ans = sum(list(map(abs, a)))
	print(ans)
else:
	# 絶対値が最小のものを負にしたものが答え
	abs_array = list(map(abs, a))
	ans = sum(abs_array) - 2 * min(abs_array)
	print(ans)
