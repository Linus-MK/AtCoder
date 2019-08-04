s = input()
n = len(s)
ans = [0] * n

s += "R"

pos_LR = -1

for i in range(n):
	if (s[i] == "R" and s[i+1] == "L"):
		pos_RL = i

	if (s[i] == "L" and s[i+1] == "R"):
		length = i - pos_LR

		pos_LR = i

		bigger = int(length // 2) + length % 2
		smaller = length - bigger

		if (i - pos_RL) % 2 == 1:
			ans[pos_RL] = smaller
			ans[pos_RL+1] = bigger
		else:
			ans[pos_RL] = bigger
			ans[pos_RL+1] = smaller


ans = map(str, ans)
print(" ".join(ans))
