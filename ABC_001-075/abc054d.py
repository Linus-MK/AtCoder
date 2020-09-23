# dp[i][j] := Aをiグラム、Bをjグラムちょうど買うための最小予算。
# i <= N * a_i <= 40*10=400
# j <= N * b_i <= 40*10=400
# ……だとダメだわ。マスの遷移が許されるかどうかの情報が入ってない。
# （ある薬品を2回使うことはできないから、薬品を買ったか否かの情報を入れなきゃいけない）
# dp[k][i][j] := k番目までの薬品を使って、Aをiグラム、Bをjグラムちょうど買うための最小予算。
# 40*400*400で、各マスの計算は2個のマスを参照すれば求まるから、
# 40*400*400*2 = 12800000 = 1280万 間に合う。

# Python TLE, PyPyで319ms

n, a_ratio, b_ratio = list(map(int, input().split()))
chemicals = [list(map(int, input().split())) for _ in range(n)]

inf = 10 ** 10
ab_max = 10
dp = [[[inf for j in range(n * ab_max + 1)] for i in range(n * ab_max + 1)] for k in range(n)]

dp[0][0][0] = 0
dp[0][chemicals[0][0]][chemicals[0][1]] = chemicals[0][2]

for k in range(1, n):
    for i in range(n * ab_max + 1):
        for j in range(n * ab_max + 1):
            if i-chemicals[k][0] >= 0 and j-chemicals[k][1] >= 0:
                dp[k][i][j] = min(dp[k-1][i][j],  dp[k-1][i-chemicals[k][0]][j-chemicals[k][1]] + chemicals[k][2])
            else:
                dp[k][i][j] = dp[k-1][i][j]

ans = inf
bai = 1
while(a_ratio * bai <= n * ab_max and b_ratio * bai <= n * ab_max):
    ans = min(ans, dp[n-1][a_ratio * bai][b_ratio * bai])
    bai += 1

if ans < inf:
    print(ans)
else:
    print(-1)
