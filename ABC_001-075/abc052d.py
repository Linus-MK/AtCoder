n, a, b = list(map(int, input().split()))
nums = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    ans += min(a*(nums[i+1]-nums[i]), b)
print(ans)
