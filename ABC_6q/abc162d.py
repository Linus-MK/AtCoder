n = int(input())
s = input()

# R, G, Bの順
# [n + 10][2][2][2]
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(n+10)]

dp[0][0][0][0] = 1
for i in range(n):
    ch = s[i]
    
    for p in range(2):
        for q in range(2):
            for r in range(2):
                dp[i+1][p][q][r] = dp[i][p][q][r]

    if ch == 'R':
        dp[i+1][1][0][0] += dp[i][0][0][0]
        dp[i+1][1][1][0] += dp[i][0][1][0]
        dp[i+1][1][0][1] += dp[i][0][0][1]
        dp[i+1][1][1][1] += dp[i][0][1][1]
    elif ch == 'G':
        dp[i+1][0][1][0] += dp[i][0][0][0]
        dp[i+1][0][1][1] += dp[i][0][0][1]
        dp[i+1][1][1][0] += dp[i][1][0][0]
        dp[i+1][1][1][1] += dp[i][1][0][1]
    else:
        dp[i+1][0][0][1] += dp[i][0][0][0]
        dp[i+1][1][0][1] += dp[i][1][0][0]
        dp[i+1][0][1][1] += dp[i][0][1][0]
        dp[i+1][1][1][1] += dp[i][1][1][0]

ans = dp[n][1][1][1]

# ans = s.count('R') * s.count('G') * s.count('B')

# print(ans)

for i in range(n-2):
    for j in range(i+1, n-1):
        k = j + (j - i)
        if k >= n:
            break
        if s[i] != s[j] != s[k] != s[i]:
            ans -= 1
            # print(i,j,k)


print(ans)
