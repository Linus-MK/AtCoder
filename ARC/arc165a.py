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

n_case = int(input())
for i_case in range(n_case):
    n = int(input())

    factor = factorize(n)
    
    temp = 0
    for k, v in factor.items():
        temp += k ** v
    if temp < n:
        print("Yes")
    else:
        print("No")
