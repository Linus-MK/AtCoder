# 2020年6月17日

# 修行という概念がない場合、消化コストを大から小に並べて食べにくさを小から大に並べて順にマッチングさせれば良い。
# そうでない状態から2つを交換したときに最大値が下がる方向にしか行かないため。

# 修行をするなら最大値を引き下げるところに修行をするのが最適なので、
# 無修行状態の結果を優先度付きキューに入れる→K回最大値を取り出してコストを引いて再投入→を繰り返す。
# 本当か? やってるうちに最適な組み合わせが変わらないか? →変わらない。食べにくさを昇順に並べたときに消化コストが降順になるのが最善手なので。
# あとKが大きいのでこれだと間に合わない。

# 決め打ち二分探索か?
# あ、それだわ。

# Python TLE 2秒以上
# PyPy 287ms

n, k = map(int, input().split())
people = list(map(int, input().split()))
foods = list(map(int, input().split()))

# 食べにくさは昇順（小から大）、人間は降順（大から小）
foods.sort()
people.sort(reverse=True)

def is_valid(time):
    # k回以下の修行で実現可能か

    n_train = 0
    for i in range(n):
        if foods[i] * people[i] <= time:
            pass
        else:
            n_train += people[i] - time // foods[i]
    
    return n_train <= k


time_ok = 2 * 10 ** 12
time_ng = -1  # 計算上、is_valid(-1) = Trueになることはあるが、二分探索の方法から言ってこれで正しいはず

while abs(time_ok - time_ng) > 1:
    mid = (time_ok + time_ng) // 2
    if is_valid(mid):
        time_ok = mid
    else:
        time_ng = mid

print(time_ok)
