# 赤色の防止をかぶっている人だけを見ると、その人の発言した人数は前から順に0, 1, ……となる。

# 1次元DP
# k人目までの帽子の組み合わせをdp[k]としよう。
# 
# dp[k] = dp[k-1] * (ここまでと整合する色の数)

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
# dp[0] = 3
current = [0, 0, 0]
mod = 10**9+7

for i in range(0, n):
    count = current.count(nums[i])
    if i == 0:
        dp[i] = 1 * count
    else:
        dp[i] = dp[i-1] * count
    dp[i] %= mod

    for j in range(3):
        if current[j] == nums[i]:
            current[j] += 1
            break
    # print(current)

print(dp[n-1])
