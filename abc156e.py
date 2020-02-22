n, k = list(map(int, input().split()))

mod = 10**9 + 7

mod = 10**9 + 7

# x ** a をmodで割った余りを、O(log(a))時間で求める。
def power(x, a):
	if a == 0:
		return 1
	elif a == 1:
		return x
	elif a % 2 == 0:
		return power(x, a//2) **2 % mod
	else:
		return power(x, a//2) **2 * x % mod

# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
	return power(x, mod-2)

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
	return (factori_table[n] * factori_inv_table[k] * factori_inv_table[n-k]) % mod

if k >= n-1:
    # nHn = 2n-1 C n
    print(binomial_coefficients(2 * n - 1, n))
else:
    # 移動がk回←→ 人数0の部屋がk個以下
    # 人数0の部屋がちょうどj個のものは
    # nCj(人数0の部屋の選び方) * jH(n-j) (余剰のj人を残りの部屋に入れる)
    ans = 0
    for j in range(k):
        if j == 0:
            ans += 1
        else:
            ans += binomial_coefficients(n, j) * binomial_coefficients(n-1, j-1) 
            ans %= mod
    print(ans)

