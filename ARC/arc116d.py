
max_len = 400010  # 適宜変更する
mod = 998244353


def modinv(x):
    '''
    xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
    Python標準のpowは割った余りを出すことも可能。
    '''
    return pow(x, mod-2, mod)


# 二項係数の左側の数字の最大値を max_len　とする。nとかだと他の変数と被りそうなので。
# factori_table = [1, 1, 2, 6, 24, 120, ...] 要は factori_table[n] = n!
# 計算時間はO(max_len * log(mod))
modinv_table = [-1] * (max_len + 1)
modinv_table[0] = None  # 万が一使っていたときにできるだけ早期に原因特定できるようにしたいので、Noneにしておく。
factori_table = [1] * (max_len + 1)
factori_inv_table = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    factori_table[i] = factori_table[i-1] * (i) % mod

modinv_table[1] = 1
for i in range(2, max_len + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod
    factori_inv_table[i] = factori_inv_table[i-1] * modinv_table[i] % mod


def binomial_coefficients(n, k):
    '''
    n! / (k! * (n-k)! )
    0 <= k <= nを満たさないときは変な値を返してしまうので、先にNoneを返すことにする。
    場合によっては0のほうが適切かもしれない。
    '''
    if not 0 <= k <= n:
        return None
    return (factori_table[n] * factori_inv_table[k] * factori_inv_table[n-k]) % mod

n, m = list(map(int, input().split()))

binomial_n = [1] * (n+1)
for k in range(0, n+1):
    binomial_n[k] = binomial_coefficients(n, k)

# 上位ビットから?下位ビットから?どっちから計算するのが良いかな……

if m % 2 == 1:
    print(0)
    exit()

# dp[bit][rest] := 今のbitにいくつ分けるか決めようとしていて、残り数がtotalでrestであるとき、何通りあるか
# dp[8][rest] = dp[4][rest] + dp[4][rest-8] + dp[4][rest-16] + …… （rest <= (1+2+4)*max_pair に対して）
# dp[8][rest] = dp[4][rest] + nC2 * dp[4][rest-8] + nC4 * dp[4][rest-16] + …… （rest <= (1+2+4)*max_pair に対して）
# 求める答えははdp[4096][total]
# コンビネーションの左は全部n なのでテーブルにするのが良い

max_pair = n // 2
total = m // 2

dp_dict = {}


digit = 1
dp_dict[digit] = [-1] * (total+1)
for rest in range(min(max_pair, total)+1):
    dp_dict[digit][rest] = binomial_n[rest*2]

digit = 2
while True:
    dp_dict[digit] = [-1] * (total+1)

    half = digit // 2
    
    for rest in range(total+1):
        temp = 0
        for k in range(max_pair + 1):
            if rest - digit * k > (digit-1) * max_pair:
                continue
            if rest - digit * k < 0:
                break
            temp += binomial_n[k*2] * dp_dict[half][rest - digit * k]

        dp_dict[digit][rest] = temp % mod
        # print(k+2, rest - digit * k)

    digit *= 2

    if digit > 2048:
        break

print(dp_dict[2048][total] % mod)
# print(dp_dict)