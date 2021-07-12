n, x = list(map(int, input().split()))
nums = list(map(int, input().split()))

summ = sum(nums) - n//2
if x >= summ:
    print('Yes')
else:
    print('No')
