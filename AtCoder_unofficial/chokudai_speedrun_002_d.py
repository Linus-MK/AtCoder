n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for num in nums:
    ans += max(num)

print(ans)