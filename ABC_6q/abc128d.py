n, k = list(map(int, input().split() ))
values = list(map(int, input().split() ))
ans = 0

left_pop_max = min(k, n)
for left in range(left_pop_max+1):
	picked_l = values[:left]

	# right_pop_max = min(k-left, n-left)
	right_pop_max = left_pop_max - left
	for right in range(right_pop_max+1):
		# rightが0だとvalues[0:]が配列全体になってしまうので
		if (right > 0):
			picked = picked_l + values[-right:]
		else:
			picked = picked_l

		picked.sort()
		push_max = min(k - left - right, left + right)
		push_val_sum = 0
		for i in range(push_max):
			if picked[i] >= 0:
				break
			push_val_sum += picked[i]

		new_ans = sum(picked) - push_val_sum
		ans = max(ans, new_ans)

print(ans)
