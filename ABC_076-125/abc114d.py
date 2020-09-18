# 

def factorize(n):
    '''
    タプルの配列と思ったけど逐次割り算する過程で次数を増やせないじゃん。
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

n = int(input())

if n <= 9:
    print(0)
    exit()

# めんどいから掛けてしまえ。間に合うだろ
import math
product = math.prod(range(1, n+1))  # python 3.8以降で使用可能
d = factorize(product)
factor = list(d.items())

# print(factor)

ans = 0
for i in range(len(factor)):
    for j in range(i+1, len(factor)):  # iとjを入れ替えたものは同一なので、i < jとなるものだけを数える。
        for k in range(len(factor)):
            if factor[i][1] >= 4 and factor[j][1] >= 4 and factor[k][1] >= 2 and i!=j and j!=k and k!=i:
                ans += 1

for i in range(len(factor)):
    for j in range(len(factor)):
            if factor[i][1] >= 4 and factor[j][1] >= 14 and i!=j:
                ans += 1

for i in range(len(factor)):
    for j in range(len(factor)):
            if factor[i][1] >= 2 and factor[j][1] >= 24 and i!=j:
                ans += 1

for i in range(len(factor)):
    if factor[i][1] >= 74:
                ans += 1

print(ans)
