n = int(input())
nums = list(map(int, input().split()))

max_now = -1
ans = 0
for i in nums:
    if i > max_now:
        ans += 1
        max_now = i
print(ans)
