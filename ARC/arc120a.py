n = int(input())
nums = list(map(int, input().split()))

maxs = [-1] * n
maxs[0] = nums[0]

cumsum = [-1] * n
cumsum[0] = nums[0]

for i in range(1, n):
    maxs[i] = max(maxs[i-1] , nums[i])
    cumsum[i] = cumsum[i-1] + nums[i]

temp = 0
for i in range(n):
    temp += cumsum[i]
    ans = (i+1) * maxs[i] + temp
    print(ans)
