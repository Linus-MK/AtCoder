# 1971ms ギリギリだな……

n, k = list(map(int, input().split()))

mod = 10**9 + 7

# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
def modinv(x):
    return pow(x, mod-2, mod)

# 二項係数の左側の数字の最大値を max_len　とする。nとかだと他の変数と被りそうなので。
# factori_table = [1, 1, 2, 6, 24, 120, ...] 要は factori_table[n] = n!
# 計算時間はO(max_len * log(mod))

max_len = 2 * n - 1 #適宜変更する

factori_table = [1] * (max_len + 1)
factori_inv_table = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    factori_table[i] = factori_table[i-1] * (i) % mod
    factori_inv_table[i] = modinv(factori_table[i])

def binomial_coefficients(n, k):
    # n! / (k! * (n-k)! )
    if k <= 0 or k >= n:
        return 1
    return (factori_table[n] * factori_inv_table[k] * factori_inv_table[n-k]) % mod

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
