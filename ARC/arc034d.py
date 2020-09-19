a, b =list(map(int, input().split()))


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

product_dict = {}
for i in range(b+1, a+1):
    factor = factorize(i)
    product_dict = factor_product(product_dict, factor)

ans = 1
for v in product_dict.values():
    ans *= (v+1)
    ans %= (10**9 + 7)

print(ans)
# print(product_dict)