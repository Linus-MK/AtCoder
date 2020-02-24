# 740ms

n, k = list(map(int, input().split()))

max_len = 2 * n - 1  # 適宜変更する
mod = 10**9 + 7


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



if k >= n-1:
    # nHn = 2n-1 C n
    print(binomial_coefficients(2 * n - 1, n))
else:
    # 移動がk回←→ 人数0の部屋がk個以下
    # 人数0の部屋がちょうどj個のものは
    # nCj(人数0の部屋の選び方) * jH(n-j) (余剰のj人を残りの部屋に入れる)
    ans = 0
    for j in range(k+1):
        if j == 0:
            ans += 1
        else:
            ans += binomial_coefficients(n, j) * binomial_coefficients(n-1, j) 
            ans %= mod
    print(ans)
