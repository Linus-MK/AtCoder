# 自明ではない全探索
# 問題条件から「最適解はこのうちのどれかだ」まで導出して、あとはその8通りを全部試すという、あんまり見かけない手法
# 番兵として十分遠いところにダミーの神社と寺をおく

a, b, q = list(map(int, input().split()))

inf = 10**12
shrines = [int(input()) for _ in range(a)]
temples = [int(input()) for _ in range(b)]

shrines = [-inf] + shrines + [inf]
temples = [-inf] + temples + [inf]

import bisect
for _ in range(q):
    pos = int(input())
    s_i = bisect.bisect(shrines, pos)
    t_i = bisect.bisect(temples, pos)

    ans = inf
    for s_j in (s_i-1, s_i):
        for t_j in (t_i-1, t_i):
            ans = min(ans, abs(shrines[s_j] - pos) + abs(temples[t_j] - shrines[s_j]))
            ans = min(ans, abs(temples[t_j] - pos) + abs(shrines[s_j] - temples[t_j]))
    print(ans)
    