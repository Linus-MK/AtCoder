# 鍵の数 Mが十分小さければ、2^Mに対してbit全探索を行えばよい
# が、今回は不可

# 逆に宝箱の数Nが十分小さいので、bitDPとなる
# dp[集合S] := S を開けるときに必要な費用の最小値。
# で、ちょうどSか? Sを含めばSより大きい集合でも良い? どっち?

# ちょうどSの場合
# dp[S] = (dp[S-Ci] + ai)の最小値 ただしCi - S != φ の場合は達成不能。
# あ、ダメだわこれじゃ。入力例3で落ちた。
# 4つ宝箱が会って、最適解は1-3-4を開ける鍵と2-3-4を開ける鍵を選ぶ場合なのに、
# ちょうど1-3-4と2の組み合わせを選んでしまった。これはダブリを考慮できていないせい。

# Sを含めばSより大きい集合でも良い場合
# dp[S]の中に書いてある鍵集合で実際にどの宝箱を開けられるかの情報が分からないので、ダメっぽい。

n, m = list(map(int, input().split()))

price = [0] * m
can_open_num = [0] * m
can_open = []
for i in range(m):
    a, b = list(map(int, input().split()))
    price[i] = a
    can_open_num = b
    can_open.append(set(map(lambda x: int(x)-1, input().split()))) # i-index → 0-index

from itertools import combinations
inf = 10 ** 10
dp = [inf for _ in range(1<<n)]
dp[0] = 0  # 空集合は0円で開けられる
for idx in range(1, 1<<n):
    digit_set = {digit for digit in range(n) if 1<<digit & idx}  # ABC041Dからコピペしてきた
    
    for key_i in range(m):
        if (can_open[key_i] - digit_set):
            continue
        # can_open[key_i]の部分集合を列挙
        whole = list(can_open[key_i])
        for num in range(len(whole) + 1):
            for can_open_subset in combinations(whole, num):

                prev_set = digit_set - set(can_open_subset)
                prev_idx = sum(1<<digit for digit in prev_set)
                dp[idx] = min(dp[idx], dp[prev_idx] + price[key_i])

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])
