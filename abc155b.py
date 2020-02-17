n = int(input())
nums = list(map(int, input().split()))

ans = 'APPROVED'

for i in nums:
    if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
        ans = 'DENIED'

print(ans)
