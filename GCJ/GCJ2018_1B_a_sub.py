# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/0000000000036601

# 解答見た。Test Set 2までの部分点解法
# →Test Set 2はTLEだった。どうして……

# DP 動的計画法
# f(a, b)を、
# 与えられた初期状態から到達可能な状態で、a番目までの選択肢に投票した人がb人であるような
# 状態すべてを考える
# その中でa番目までの四捨五入の合計の最大値はいくつか。

# 問題の答えはf(N, N)

# f(1, b) = 1番目の投票がb人 = b/N*100の四捨五入
# f(a, b)の計算
# for k in range(b-1):
#     f(a-1, k) + (b-k)/N*100の四捨五入
# で最大値を取る。
# f(a, b)でO(N)の計算時間がかかるので、全体の計算時間はO(N^3)

def my_round(x):
    return int((x * 2 + 1) // 2)
# https://note.nkmk.me/python-round-decimal-quantize/

n_testcase = int(input())
for i_test in range(n_testcase):
    n, l = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # リストの長さをnに揃える
    nums = nums + [0] * (n-l)

    # aが増えたときに加算されるのは高々100、それをn回繰り返しても負になるように
    inf = 100 * (n + 10)
    # 1-indexで書いてしまおう そのためにサイズをn+1にする
    dp = [[-inf for _ in range(n+1)] for _ in range(n+1)]

    for b in range(1, n+1):
        # round関数は偶数への丸めなので、自分で関数を定義
        if b >= nums[0]:
            dp[1][b] = my_round(b/n * 100)

    for a in range(2, n+1):
        for b in range(1, n+1):
            if b < nums[a-1]:
                continue

            temp = -inf
            for k in range(0, b - nums[a-1] + 1):
                temp = max(temp, dp[a-1][k] + my_round((b-k)/n*100))
            
            dp[a][b] = temp
    
    ans = dp[n][n]

    # print(dp)

    print("Case #{}: {}".format(i_test+1, ans))
