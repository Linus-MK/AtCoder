# tempやbが巨大になって最大公約数を求めるのが大変だからTLEになっちゃうよねー、
# ここから素因数分解を使って高速化しなきゃね……と思いながら提出したら通った。
# Python3で1330ms, PyPy3で1665msで通る（珍しくPyPyのほうが遅い）

n = int(input())
nums = list(map(int, input().split()))

import math

summ = 1
b = 1
mod = 10**9 + 7

for idx in range(1, n):
    temp = b * nums[idx-1]
    gcd = math.gcd(temp, nums[idx])
    multiple = nums[idx] // gcd
    summ *= multiple

    b = b * nums[idx-1] * multiple // nums[idx]
    summ += b
    summ %= mod

print(summ)
