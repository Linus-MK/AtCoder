n = int(input())
nums = list(map(int, input().split()))

d = {}
for i in range(n):
    d[nums[i]] = i+1

ans = []
for j in range(1, n+1):
    ans.append(str(d[j]))

print(" ".join(ans))
