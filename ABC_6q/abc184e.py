# ワープポイント（テレポーター）がなければごく普通の幅優先探索（https://atcoder.jp/contests/abc007/tasks/abc007_3）
# ワープポイントもコスト1の辺として幅優先探索をすればよい。

# なお、同じ文字のワープポイントを2度通ることはありえない。aa.....aa...だったら最初aから最後のaにワープするのが最適なので
# （換言すれば、同じ文字のワープポイントの各点は完全グラフになるので、普通に幅優先探索をすればある点の距離がdならば他の点が全て距離d+1で確定する）

# ワープポイントをどう管理するか?
from collections import deque

h, w = list(map(int, input().split()))
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
masu = []
for _ in range(h):
    masu.append(input())
distance = [[-1 for _ in range(w)] for _ in range(h)]
warp_points = set()
warp_points_char = dict()
warp_points_visited = dict()


for i in range(h):
    for j in range(w):
        if masu[i][j] == 'S':
            start_h = i
            start_w = j
        elif masu[i][j] == 'G':
            goal_h = i
            goal_w = j
        elif masu[i][j] != '.':
            warp_points.add((i, j))
            warp_points_visited[masu[i][j]] = False
            # warp_points_char[masu[i][j]] = warp_points_char.get(masu[i][j], set()).add((i, j))
            if masu[i][j] in warp_points_char:
                warp_points_char[masu[i][j]].add((i, j))
            else:
                warp_points_char[masu[i][j]] =  set([(i, j)])

queue = deque()
queue.append((start_h, start_w))
distance[start_h][start_w] = 0

import string
while len(queue) > 0:
    now_h, now_w = queue.popleft()
    
    if (now_h, now_w) in warp_points:
        # ワープポイント 同じ文字が書いてある他のマスを
        for char in warp_points_char.keys():
            if (not warp_points_visited[char]) and (now_h, now_w) in warp_points_char[char]:
                for next_h, next_w in warp_points_char[char]:
                    if (now_h, now_w) != (next_h, next_w) and distance[next_h][next_w] == -1:

                            queue.append((next_h, next_w))
                            distance[next_h][next_w] = distance[now_h][now_w] + 1
                break
                warp_points_visited[char] = True

    for dhi, dwi in zip(dh, dw):
        next_h = now_h + dhi
        next_w = now_w + dwi
        if 0 <= next_h < h and 0 <= next_w < w and distance[next_h][next_w] == -1:
            if masu[next_h][next_w] == '#':
                # pass文でも良いけど、次に他のマスの隣接点として見られることになるので、distance埋めたほうが良い
                distance[next_h][next_w] = -2
            elif (next_h, next_w) in warp_points:
                # ワープポイント 同じ文字が書いてある他のマスを
                queue.append((next_h, next_w))
                distance[next_h][next_w] = distance[now_h][now_w] + 1
            elif (next_h, next_w) == (goal_h, goal_w):
                # ゴール
                print(distance[now_h][now_w] + 1)
                # print(distance)
                exit()
            else:
                # .が書いてある通常のマス
                queue.append((next_h, next_w))
                distance[next_h][next_w] = distance[now_h][now_w] + 1

# ゴールに到達不能
print(-1)
