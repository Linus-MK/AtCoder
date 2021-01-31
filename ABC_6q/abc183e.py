# 一言で：DP＋累積和
# まぁ見るからにDPとわかる問題だけど、そのまま漸化式を書くと各マスの更新にO(H)かかるのでダメ。
# 累積和っぽくして、順次計算すれば各マスの更新がO(1)となり間に合う。
# down[i][j] := 最後の移動を下向きにして、マスi, jに移動する場合の数

h, w = list(map(int, input().split()))

masu = [input() for _ in range(h)]

# 番兵を使おう さもないとDP更新式の条件分岐が鬱陶しい
down = [[0 for _ in range(w+1)] for _ in range(h+1)]
right = [[0 for _ in range(w+1)] for _ in range(h+1)]
diag = [[0 for _ in range(w+1)] for _ in range(h+1)]
total = [[0 for _ in range(w+1)] for _ in range(h+1)]
mod = 10**9+7

total[1][1] = 1

for row in range(1, h+1):
    for col in range(1, w+1):
        if (row==1 and col==1):
            pass
        elif masu[row-1][col-1] == '#':
            down[row][col] = right[row][col] = diag[row][col] = total[row][col] = 0
        else:
            # 下に移動してrow, colに着くことから、1つ前のマスに着目して漸化式を立てる
            # down[row][col] = total[0][col] + total[1][col] + ... + total[row-1][col]
            #   = down[row-1][col] + total[row-1][col]
            down[row][col] = (down[row-1][col] + total[row-1][col]) % mod
            right[row][col] = (right[row][col-1] + total[row][col-1]) % mod
            diag[row][col] = (diag[row-1][col-1] + total[row-1][col-1]) % mod
            total[row][col] = (down[row][col] + right[row][col] + diag[row][col]) % mod
        
print(total[h][w])
