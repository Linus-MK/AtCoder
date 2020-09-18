# 使える問題：
# https://atcoder.jp/contests/abc114/tasks/abc114_d ABC114 D 756
# https://atcoder.jp/contests/abc110/tasks/abc110_d ABC110 D Factorization (まだ解いてない)
# https://atcoder.jp/contests/abc169/tasks/abc169_d ABC169 D Div Game

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
        if n % div == 0:
            n //= div
            factor[div] = factor.get(div, 0) + 1
            if n == 1:
                return factor
        else:
            div += 1

# ABC149Cより
def is_prime(num):
    if num == 1:
        raise ValueError("error!")
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True
