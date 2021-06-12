"""
操作1と2だけでは絶対に大きな数は作れない。操作3と4が重要。
状態(1, 1)から3と4を繰り返しやってみると、フィボナッチ数ができる。
さて、3と4は、長方形で考えると長方形に正方形をくっつける操作である。これ逆から考えるとユークリッドの互除法をしてるじゃん。
ユークリッドの互除法（長方形から正方形を切り取り）で大きな数を早く小さく減らしたい。
yの選び方に自由度があるのがミソ。
最初のx/yを黄金比にしておいて、そこから互除法を実行すれば、2回の操作で（1.618）^2 分の1になる。平均1回の操作で1.618 分の1になる。
1.618 ** 100 ≒ 7.9* 10**20 なので、10**18でも小さい数に落とせる。
ただし単純な黄金比だと、最終状態があまり良くなく（両者の公約数が大きい）、130回を超えるケースが存在する。10**18とかがそうなる。
yの値は正確に黄金比である必要は無いので、130回超えてたら少しyを変えてみて、130回以下なら出力する。
……何か、 Google Code Jam っぽい問題だなと思った。
"""

n = int(input())

if n <= 130:
    # 操作1をn回
    print(n)
    for i in range(n):
        print(1)
    exit()

import math
golden_ratio = (1 + math.sqrt(5))/2
# print(golden_ratio)

x = n
y_init = int(round(n / golden_ratio))

for diff in range(100):
    x = n
    y = y_init - diff
    # print(y)

    ans_rev = []
    while True:
        quot = x // y
        x = x - quot * y
        for i in range(quot):
            ans_rev.append(3)
        if x == 0:
            break
        quot = y // x
        y = y - quot * x
        for i in range(quot):
            ans_rev.append(4)
        if y == 0:
            break

    for i in range(x):
        ans_rev.append(1)
    for i in range(y):
        ans_rev.append(2)

    if len(ans_rev) <= 130:
        print(len(ans_rev))
        for ope in reversed(ans_rev):
            print(ope)
        exit()
