# 整数Nから考えるとやりづらい。
# 組の個数kから考えてみよう。
# 集合の2つの組み合わせの数は k(k-1)/2 通り。それに要素が1つずつ入るので、N = k(k-1)/2 と決まる
# あとはN個のチームの総当たり戦を作るイメージで構成すれば良い。
# kから考えるのがポイントのように思う。

# 2つTLE (N= 87990, 99681)。ケース21(55611)で1252 ms

import itertools

n = int(input())
k = 0  # 条件を満たす最小のkは1
while True:
    k+= 1
    if k*(k-1)//2 == n:
        print('Yes')
        print(k)

        combi = list(itertools.combinations(range(k), 2))
        for i in range(k):
            t = [idx+1 for idx, tup in enumerate(combi) if i in tup]
            
            print(f'{k-1} ' + ' '.join(list(map(str, t))))

        exit()
    elif k*(k-1)//2 > n:
        print('No')
        exit()


