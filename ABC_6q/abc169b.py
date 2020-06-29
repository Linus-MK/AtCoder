p = int(input())
nums = list(map(int, input().split()))

ans = 1
large = False
for i in nums:
    if i == 0:
        ans = 0
        large = False
    if not large:
        ans = ans * i
        if ans > 10 ** 18:
            large = True
    else:
        pass

if large:
    print(-1)
else:
    print(ans)
