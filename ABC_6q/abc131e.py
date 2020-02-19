n, k = list(map(int, input().split() ))

maximum = (n-1)*(n-2)//2
if(k <= maximum):
	#構成可能
	ans = n - 1 + maximum -k
	print(ans)
	# 頂点1と残りの頂点をつなぐ
	for i in range(2, n + 1):
		print("{} {}".format(1 ,i)	)

	# 頂点2以上のなかで、maximus - k 個をつなぐ
	count = n-1
	if count == ans:
		exit()
	i = 2
	j = 3
	while True:
		print("{} {}".format(i ,j)	)
		count += 1
		if count == ans:
			break
		j += 1
		if j > n:
			i += 1
			j = i+1

else:
	print(-1)
