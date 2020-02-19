n, k = list(map(int, input().split() ))
nums = list(map(int, input().split() ))

summ = sum(nums)
divisors = []

for d in range(1, summ):
	if d * d > summ:
		break
	if summ % d == 0: #約数
		divisors.append(d)
		divisors.append(int(summ // d))

divisors.sort(reverse = True)

# print(divisors)

for d in divisors:

	residues = [0] * n
	for i in range(n):
		residues[i] = nums[i] % d

	residues.sort(reverse = True)

	init_sum = sum(residues)
	num_reverse = init_sum // d

#	times_operation = 0
#	for i in range(num_reverse):
#		times_operation -= num_reverse
	times_operation = d * num_reverse - sum(residues[0:num_reverse])

# 	print(d, residues, num_reverse,  times_operation)

	if times_operation <= k:
		print(d)
		exit()
