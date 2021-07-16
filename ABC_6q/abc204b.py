n = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    ans += max(num - 10, 0)
print(ans)
