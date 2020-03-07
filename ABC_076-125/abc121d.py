a, b = list(map(int, input().split()))

# cumlative_xor(a) を 0　から a までのxorの結果とする。
# 求める答えは、cumlative_xor(b) xor cumlative_xor(a-1) （累積XOR）

def cumlative_xor(a):
	ans = 0
	if a % 4 == 1 or a % 4 == 2 :
		ans = 1

	for i in range(1, 41):
		# 10**12 < 2**40 なので
		temp = 2 ** i
		if a & 1 == 0 and a & temp > 0:
		# if a % 2 == 0 and a % (temp * 2) >= temp: と同値。
			ans = ans | temp

	return ans

print(cumlative_xor(b) ^ cumlative_xor(a-1))
