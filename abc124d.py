n, k = list(map(int, input().split()))
s = input()

end = []
start = []

if s[0] == "1":
	start.append(0)
else:
	#仮想的な1の区間を作る
	start.append(0)
	end.append(0)

for i in range(n-1):
	if s[i] == "1" and s[i+1] == "0":
		end.append(i)
for i in range(1, n):
	if s[i-1] == "0" and s[i] == "1":
		start.append(i)

if s[-1] == "1":
	end.append(n-1)
else:
	#仮想的な1の区間を作る
	start.append(n-1)
	end.append(n-1)

ans = 0

for j in range(len(start) - k):
	temp = end[j+k] - start[j] + 1 
	if temp > ans:
		ans = temp

if len(start) <= k:
	ans = n

print(ans)
