# 使える問題：
# https://atcoder.jp/contests/abc114/tasks/abc114_d ABC114 D 756
# https://atcoder.jp/contests/abc110/tasks/abc110_d ABC110 D Factorization (まだ解いてない)
# https://atcoder.jp/contests/abc169/tasks/abc169_d ABC169 D Div Game
# https://atcoder.jp/contests/arc034/tasks/arc034_3 ARC034 C 約数かつ倍数

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


def factor_product(a, b):
    '''
    素因数分解のdict a, bを受け取って、
    積に対応するdictを返す
    '''
    product = a.copy()
    for k, v in b.items():
        product[k] = product.get(k, 0) + v
    return product

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

# 約数列挙
# ABC136Eより
def get_divisors(num):
    if num == 1:
        return [1]
    
    divisors = []
    for d in range(1, num):
        if d * d > num:
            break
        if num % d == 0: #約数
            divisors.append(d)
            if d * d != num:  # numの平方根の場合は重複するので追加しない
                divisors.append(int(num // d))

    return divisors

# 最初「最小の素因数を全部かければ良いのかな。約数列挙して小さい方から2番目（1を除く）を列挙して、集合型に入れてかければ良さそう」と思ったけど
# WAだった。例えば「3 6」だと正解は3なのに、6と出力してしまう。
# 素数だけ避けておいて、合成数だけ最初に見る。これなら適当に上限きめて全探索でも行けるでしょう。
# 多分2*3*5*7が上限だと思う（7*7=49が、素数の2乗で50以下となる最大のものだから）
# であとは素数を別に考えれば良い。例えば37が出てきたらそれは37を掛けるしか無い。

n = int(input())
nums = list(map(int, input().split()))

primes = [num for num in nums if is_prime(num)]
products = [num for num in nums if not is_prime(num)]

if len(products) == 0:
    candi = 1
else:
    for candi in range(2, 10000):
        ok = True
        candi_divis = set(get_divisors(candi))
        for p in products:
            p_divis = set(get_divisors(p))
            if len(candi_divis & p_divis) == 1:
                ok = False
                break
        if ok:
            break

ans = candi
for p in primes:
    if ans % p != 0:
        ans *= p

print(ans)
