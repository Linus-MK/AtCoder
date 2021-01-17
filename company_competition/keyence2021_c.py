# dp[i][j] := i, jのマスに到達するような移動経路 の和か……?
# だとすると全体は3^(HW-K)だから、例えば一番左上が未記入だったら、(2, 1)に全ての場合に行けるから、3^(HW-K)だわ。
# 違うわ、左上がD,XだったらOKでRだったら不可だから、3^(HW-K) * 2 / 3だわ。何か変な気がする。それは。
# いやでもこっちのほうが簡単か。3の逆元を作れば良いから。
# こっちでやる！！

h, w, k = list(map(int, input().split()))

# masu = [['-' for _ in range(w)] for _ in range(h)]
masu_dict = {}
for i in range(k):
    h0, w0, char = input().split()
    masu_dict[(int(h0)-1, int(w0)-1)] = char
    # masu[int(h0)-1][int(w0)-1] = char

# 当該のマスに応じて次のマスに行けるかどうかが決まるので、配るDPで書いたほうがよい。
# 集めるDPだと上のマスと左のマスに応じて当該マスをどうするかになるので二度手間っぽい。

mod = 998244353
# rev_3 = pow(3, -1, mod)  # PyPyだと不可
rev_3 = pow(3, mod-2, mod)
rev_3_times_2 = (2 * rev_3) % mod
dp = [[0 for _ in range(w+1)] for _ in range(h+1)]  # 番兵として一番右と一番下に一行一列追加

dp[0][0] = pow(3, h*w-k, mod)
for row in range(h):
    for col in range(w):
        dp[row][col] = dp[row][col] % mod

        ch = masu_dict.get((row, col), '-')
        if ch == 'D':
            dp[row+1][col] += dp[row][col]
        elif ch == 'R':
            dp[row][col+1] += dp[row][col]
        elif ch == 'X':
            dp[row+1][col] += dp[row][col]
            dp[row][col+1] += dp[row][col]
        else:
            # 3^(HW-K)通りの全ての盤面を考えよう。このうち、下に進めるのはこのマスにD,Xを書いた 3^(HW-K) * 2 / 3とおりである。
            # つまり全体の3分の2とすれば良い。右についても同様。
            # dp[row+1][col] += dp[row][col] * 2 / 3
            # dp[row][col+1] += dp[row][col] * 2 / 3
            temp = (dp[row][col] * rev_3_times_2) % mod
            dp[row+1][col] += temp
            dp[row][col+1] += temp

print(dp[h-1][w-1] % mod)

# dp[i][j] := (1, 1)から(i, j)のマスまでの長方形のマスの未記入をtとしたとき、3^t通りについて(i, j)に到達するような移動経路の場合の数の和
# にしよう。
# dp[i][j-1]からdp[1][j]に行くには?
# 盤面のうちdp(i, j)の真上方向の'-'の数
# 盤面のうちdp(i, j)の真左方向の'-'の数
# が必要になる。ややこしいのでやめとこう。


