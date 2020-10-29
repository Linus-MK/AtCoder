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

n, k = list(map(int, input().split()))
if n == 1:
    print(-1)
    exit()

d = factorize(n)
max_len = sum([power for power in d.values()])

if k > max_len:
    print(-1)
else:
    ans_list = []
    for i in range(k-1):
        min_div = min(d.keys())
        n //= min_div
        ans_list.append(min_div)
        if d[min_div] == 1:
            del d[min_div]
        else:
            d[min_div] -= 1
    
    ans_list.append(n)

    ans_str = list(map(str, ans_list))
    print(' '.join(ans_str))
