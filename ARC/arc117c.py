# パスカルの三角形を3で割ったあまり……とはちょっと違う。
# O NlogNで解かないといけないから、1つずつ埋めてるとダメ

# 3つは全て対等。それを入れ替えたら、答えも入れ替えたものになる

# 不変量に注目じゃないかなー……


max_len = 400100  # 適宜変更する
mod = 3


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


n = int(input())
string = input()

ans = 0
for i in range(n):
    char = string[i]

    if char == 'W':
        a = 1
    elif char == 'B':
        a = 2
    elif char == 'R':
        a = 0
    
    ans += a * binomial_coefficients(n-1, i)

ans = ans % 3
ans *= pow(-1, n-1)
print('RBW'[ans])


