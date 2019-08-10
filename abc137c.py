n = int(input())

strings = [input() for _ in range(n)]

st2 = [[]] * n
for i in range(n):
	st2[i] = sorted(strings[i])
st2.sort()

ans = 0
same = 1
for i in range(1, n):
	if st2[i] == st2[i-1]:
		same += 1
	else:
		ans += int(same * (same-1)//2)
		same = 1

ans += int(same * (same-1)//2)
print(ans)
