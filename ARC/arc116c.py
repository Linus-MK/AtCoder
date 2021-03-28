# 最後の数が何になるかで場合分けだろう。
# 例えば最後の数が100=2^2 5^2だったら?
# どこで数を増やすか。重複組合せのHで求まる。正解の前に1が補完されてると考えるとわかりやすい
# n+1 H 2 * n+1 H 2 = n+3 C 2 * n+3 C 2

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


def binomial_coefficients2(n, k):
    '''
    (n * (n-1) * ... * (n-k+1)) / (1 * 2 * ... * k)
    '''
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


def factorize(n):
    '''
    素因数分解をする。
    タプルの配列にしようと思ったけど、逐次割り算する過程で次数を増やせないじゃん。
    二重配列?
    dictにしよう。
    '''
    if n == 1:
        raise('n >= 2')
    
    factor = {}
    div = 2
    while True:
        if div * div > n:
            factor[n] = factor.get(n, 0) + 1
            return factor

        if n % div == 0:
            n //= div
            factor[div] = factor.get(div, 0) + 1
        else:
            div += 1

n, m = list(map(int, input().split()))


ans = 1 # last_num=1
for last_num in range(2, m+1):
    factor = factorize(last_num)
    ans_current = 1
    for k, v in factor.items():
        # ans_current *= n+v-1 C v
        ans_current *= binomial_coefficients(n+v-1, v)
    ans += ans_current

print(ans % mod)
