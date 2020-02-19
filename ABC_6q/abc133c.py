l, r = list(map(int, input().split()))
mod = 2019

if (r - l >= mod):
	print(0)
	exit()

l = l % mod
r = r % mod
if r < l:
	r += mod 

ans = mod * mod
for i in range(l, r+1):
	for j in range(i+1, r+1):
		temp = i * j % 2019
		ans = min(temp, ans)

print(ans)
