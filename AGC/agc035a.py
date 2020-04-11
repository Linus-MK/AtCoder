# 全て0ならTrue
# Nが3の倍数かつ、配列が「aがm個とbがm個とcがm個」かつ、a^b == c ならTrue
# それ以外はFalse

n = int(input())
nums = list(map(int, input().split()))

if max(nums) == 0:
    print('Yes')
    exit()

if n % 3:
    print('No')
    exit()

m = n // 3
nums.sort()
for i in range(m-1):
    if nums[i] != nums[i+1] or nums[m+i] != nums[m+i+1] or nums[2*m+i] != nums[2*m+i+1]:
        print('No')
        exit()

if nums[0] ^ nums[m] == nums[2*m]:
    print('Yes')
else:
    print('No')
