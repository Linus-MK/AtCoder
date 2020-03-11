# bit全探索
# 1130ms 半端にnumpyを使うと却って遅い！

n = int(input())
eigyou = [list(map(int, input().split())) for _ in range(n)]
profits = [list(map(int, input().split())) for _ in range(n)]
# 全休業を除く = 0を除外して、1〜1023まで回す
# 10 = 0000001010 ならば、木曜午前と金曜午前に営業することを示す

ans = -(10 ** 7) * 100 - 10
for i in range(1, 2**10):
    eigyou_here = [-1] * 10
    temp = 0
    for digit in range(10):
        eigyou_here[10 - 1 - digit] = int(i & (2 ** digit) > 0)
    for j_shop in range(n):
        import numpy as np
        coincide_time = np.dot(eigyou[j_shop], eigyou_here)
        # for time in range(10):
        #     coincide_time += eigyou[j_shop][time] * eigyou_here[time]
        temp += profits[j_shop][coincide_time]

    ans = max(ans, temp)

print(ans)
