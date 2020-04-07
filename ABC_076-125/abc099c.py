# 1次元DP
# 番兵を手前に100000用意してしまおうｗ
n = int(input())

dp = [9999] * (200000 + 10)
offset = 100000
dp[0 + offset] = 0

coin = []
coin.append(1)
temp = 6
while temp <= 100000:
    coin.append(temp)
    temp *= 6
temp = 9
while temp <= 100000:
    coin.append(temp)
    temp *= 9

# print(coin)

for i in range(1, len(dp) - offset):
    temp_min = 9999
    for c in coin:
        temp_min = min(temp_min, dp[i + offset - c])
    dp[i + offset] = temp_min + 1

print(dp[n + offset])
