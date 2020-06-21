# 全縦線と全横線を全探索するとO(N^5)
# 50 ** 5 = 312500000
# 縦線の選び方は50 C 2だから2分の1になるのを考慮しても、78125000
# いや無理だろ……と思ったら公式がこの解法だった。衝撃。
# 二次元累積和を使うと各回の計算がO(1)になるので、O(N^4)となる。

# まず O(N^5)解法を作ってみよう。通るのかこれ?
# Python 3.8.2 ではTLE、PyPyではAC(1.2秒)

n, k = list(map(int, input().split()))
coords = [list(map(int, input().split())) for _ in range(n)]

ans = (3 * 10 ** 9) ** 2
for ix1, x1 in enumerate(coords):
    for ix2, x2 in enumerate(coords[ix1+1:]):
        for iy1, y1 in enumerate(coords):
            for iy2, y2 in enumerate(coords[iy1+1:]):
                point_in_rect = 0
                for c in coords:
                    # ソートしてない。
                    if (c[0] - x1[0]) * (c[0] - x2[0]) <= 0 and (c[1] - y1[1]) * (c[1] - y2[1]) <= 0:
                        point_in_rect += 1
                if point_in_rect >= k:
                    ans = min(ans, abs((x1[0] - x2[0]) * (y1[1] - y2[1])))

print(ans)
