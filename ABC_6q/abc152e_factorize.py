# tempやbが巨大になるので、素因数分解で持っておくパターン

n = int(input())
nums = list(map(int, input().split()))

def factorize(n):
    if n == 1:
        return dict()
    
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


def factor_quotient(a, b):
    '''
    素因数分解のdict a, bを受け取って、
    商に対応するdictを返す
    !!!割り切れない場合はおかしくなる!!!
    '''
    quotient = a.copy()
    for k, v in b.items():
        quotient[k] = quotient.get(k, 0) - v
    return quotient


def factor_gcd(a, b):
    '''
    素因数分解のdict a, bを受け取って、
    gcd（最大公約数）に対応するdictを返す
    '''
    gcd = dict()
    for k, v in a.items():
        if k in b:
            gcd[k] = min(b[k], v)
    return gcd


def calc_product(d):
    ans = 1
    for k, v in d.items():
        ans *= k ** v
    return ans


def calc_product_mod(d, mod):
    ans = 1
    for k, v in d.items():
        ans *= k ** v
        ans %= mod
    return ans


import math

summ = 1
b = dict()
mod = 10**9 + 7

for idx in range(1, n):

    # temp = b * nums[idx-1]
    temp = factor_product(b, factorize(nums[idx-1]))
    # gcd = math.gcd(temp, nums[idx])
    num_idx = factorize(nums[idx])
    gcd = factor_gcd(temp, num_idx)

    # multiple = nums[idx] // gcd
    multiple = factor_quotient(num_idx , gcd)
    # summ *= multiple
    summ *= calc_product(multiple)

    # b = temp * multiple // nums[idx]
    #   = temp // gcd
    b = factor_quotient(temp, gcd)
    
    summ += calc_product_mod(b, mod)
    summ %= mod

print(summ)
