nums = list(map(int, input().split()))

summ = sum(nums)
half = -1
if summ % 2 == 0:
    half = summ / 2

ans = 'No'
for i in range(16):
    temp = 0
    for idx  in range(3):
        if i & 2**idx:
            temp += nums[idx]
    if temp == half:
        ans = 'Yes'

print(ans)
