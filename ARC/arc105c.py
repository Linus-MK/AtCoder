# Nがすごい小さい N!を全探索できるぞ
# ただしN! = 40000　なのでMとかけるとダメ

n_camel, m_bridge = list(map(int, input().split()))
weights = list(map(int, input().split()))

parts = [list(map(int, input().split())) for _ in range(m_bridge)]

min_limit = min([x[1] for x in parts])
if max(weights) > min_limit:
    print(-1)
    exit()

import itertools
import bisect

ans = 10 ** 10

parts.sort(key= lambda x: x[1])
vvv = [x[1] for x in parts]
lll = [x[0] for x in parts]
for i in range(1, m_bridge):
    lll[i] = max(lll[i], lll[i-1])

for narabi in itertools.permutations(range(n_camel), n_camel):
    # 累積和
    w_cumsum = [0] * (n_camel+1)
    for cam in range(n_camel):
        w_cumsum[cam+1] = w_cumsum[cam] + weights[narabi[cam]]
    # print(narabi)
    # print(w_cumsum)

    pos = [0] * n_camel

    for i in range(1, n_camel):
        # narabi[i] の場所を決める。
        for start in range(0, i):  # 2つ以上の要素の和だけ見れば良いので
            weight_concerned = w_cumsum[i+1] - w_cumsum[start]
            # limit = max length such that v < weight_conserned
            idx = bisect.bisect(vvv, weight_concerned) - 1
            limit = 0
            if idx >= 0:
                limit = lll[idx]

            pos[i] = max(pos[i], pos[start] + limit)
    
    # print(pos[-1])
    ans = min(ans, pos[-1])

print(ans)
