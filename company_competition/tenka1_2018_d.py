# 整数Nから考えるとやりづらい。
# 組の個数kから考えてみよう。
# 集合の2つの組み合わせの数は k(k-1)/2 通り。それに要素が1つずつ入るので、N = k(k-1)/2 と決まる
# あとはN個のチームの総当たり戦を作るイメージで構成すれば良い。
# kから考えるのがポイントのように思う。

# TLEは消えた。実行時間104ms
# combi自体は悪くない。combiを何周もイテレートすると計算量がO(k^3)=O(N√N)になって厳しい。
# combiを1周にして計算量をO(k^2)=O(N)に抑える。

import itertools

n = int(input())
k = 0  # 条件を満たす最小のkは1
while True:
    k+= 1
    if k*(k-1)//2 == n:
        print('Yes')
        print(k)

        combi = itertools.combinations(range(k), 2)

        dict_ = {i: [] for i in range(k)}
        for idx, tup in enumerate(combi):
            a = tup[0]
            dict_[a].append(idx+1)
            b = tup[1]
            dict_[b].append(idx+1)

        for i in range(k):
            print(f'{k-1} ' + ' '.join(list(map(str, dict_[i]))))

        exit()
    elif k*(k-1)//2 > n:
        print('No')
        exit()
