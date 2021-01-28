aa, bb, cc = list(map(int, input().split()))

dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for a in range(100, -1, -1):
    for b in range(100, -1, -1):
        for c in range(100, -1, -1):
            if a == 100 or b == 100 or c == 100:
                dp[a][b][c] = 0
            elif a == 0 and b == 0 and c == 0:
                pass  # 考慮しなくて良い
            else:
                s = a+b+c
                dp[a][b][c] = dp[a+1][b][c] * (a/s) + dp[a][b+1][c] * (b/s) + dp[a][b][c+1] * (c/s) + 1


print(dp[aa][bb][cc])
