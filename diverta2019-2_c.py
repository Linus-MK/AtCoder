n = int(input())
nums = list(map(int, input().split() ))
nums.sort()

if nums[0] >= 0:
	# all 0以上
	print(sum(list(map(abs, nums))) - 2 * nums[0])

	hikareru = nums[0]
	for idx in range(2,n):
		print("{} {}".format(hikareru, nums[idx]) )
		hikareru -= nums[idx]

	print("{} {}".format(nums[1], hikareru) )

elif nums[-1] <= 0:
	# all 0以下
	print(sum(list(map(abs, nums))) - 2 * (-1)*nums[-1] )

	hikareru = nums[-1]
	for idx in range(n-1):
		print("{} {}".format(hikareru, nums[idx]) )
		hikareru -= nums[idx]

else:
	print(sum(list(map(abs, nums))) )

	hikareru = nums[0]
	idx = n-2
	while True:
		if nums[idx] < 0:
			break
		print("{} {}".format(hikareru, nums[idx]) )
		hikareru -= nums[idx]
		idx -= 1

	hiku = hikareru
	print("{} {}".format(nums[n-1], hiku) )
	hikareru = nums[n-1] -  hiku

	idx = 1
	while True:
		if nums[idx] >= 0:
			break
		print("{} {}".format(hikareru, nums[idx]) )
		hikareru -= nums[idx]
		idx += 1
