N = int(input())
S = input()

# 白→黒　が許容される状態

ans = N + 1

# 所与→全黒
ans = S.count(".")
prev = ans

for i in range(N):
	if S[i] == "#":
		now = prev + 1
	else:
		now = prev - 1


	if now < ans:
		ans = now
	prev = now

print(ans)
