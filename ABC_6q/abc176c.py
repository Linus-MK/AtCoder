n = int(input())
nums = list(map(int, input().split()))

ans = 0
maximum = 0
for num in nums:
    maximum = max(maximum, num)
    ans += maximum - num

print(ans)
