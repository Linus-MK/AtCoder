# 公式解説ないじゃん……
# 以下2つでは「各数に10^9をかけて、条件を『2つをかけて10^18で割り切れる』とする」と読み替えている。そっちのほうが分かりやすいなー。
# 負の添字で混乱せずに済む。
# https://tiramistercp.hatenablog.com/entry/agc047-a
# https://www.hamayanhamayan.com/entry/2020/08/10/054247

# 最初、TLEの原因を推測するのを間違えたね。
# 2と5の素因数の数だけ分かれば十分なのに、割鶏牛刀の素因数分解をしてしまったのがTLEの原因。
# この場合の計算量的に最悪のケースは
# 1234.123456789
# のような場合。13桁の数を素因数分解する必要があり、これが素数だと10^(6.5)くらいまで割らないと素数判定できない。
# 時間がかかりすぎる。だからTLEになるのだ。
# 掛け算の相方を探すところは累積和を使おうが使うまいがほとんど計算時間に影響はない。
# 所詮20^3か20^4かの違いなので。20^4=160000なので。

n = int(input())

def factorize(n):
    '''
    素因数分解をする。
    タプルの配列にしようと思ったけど、逐次割り算する過程で次数を増やせないじゃん。
    二重配列?
    dictにしよう。
    →2と5の素因数の数がわかれば良いので、div > 5ならその時点でリターン
    '''
    if n == 1:
        # raise('n >= 2')
        return {}
    
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

            if div > 5:
                return factor


count_dict = {}

for i in range(n):
    string = input()
    dot_pos = string.find('.')
    if dot_pos == -1:
        # 小数点がない = 整数
        fraction_len = 0
    else:
        fraction_len = len(string) - dot_pos - 1
    
    x = int(string.replace('.', ''))
    factor = factorize(x)
    factor_2 = factor.get(2, 0) - fraction_len
    factor_2 = min(9, factor_2)
    factor_5 = factor.get(5, 0) - fraction_len
    factor_5 = min(9, factor_5)

    count_dict[(factor_2, factor_5)] = count_dict.get((factor_2, factor_5), 0) + 1

# print(count_dict)

ans = 0
for i in range(-9, 9+1):
    for j in range(-9, 9+1):
 
        count = count_dict.get((i, j), 0)
        if count > 0:
            temp = 0
            for factor_2 in range(-i, 9+1):
                for factor_5 in range(-j, 9+1):
                    temp += count_dict.get((factor_2, factor_5), 0)
            if i >= 0 and j >= 0:
                temp -= 1
            ans +=  count * temp
 
print(ans//2)
