# 長い間考えて分からなかったけど、ようやく方針が分かった。
# 始点を複数にした幅優先探索
# 距離1の点をキューに入れる、
# 距離1の点を出しながら距離2の点をキューに入れる、
# 以下略。でできるじゃん。

# Python TLE, PyPy3 443ms(制限時間1秒)

h, w = list(map(int, input().split()))

masu = [input() for i in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

distance = [[-1 for _ in range(w)] for _ in range(h)]

from collections import deque

queue = deque([])
for i in range(h):
    for j in range(w):
        if masu[i][j] == '#':
            distance[i][j] = 0
            queue.append((i, j))

ans = 0
while True:
    if len(queue) == 0:
        break
    now = queue.popleft()
    now_h = now[0]
    now_w = now[1]
    now_distance = distance[now_h][now_w]
    # print(now_h, now_w)

    for i in range(4):
        next_h = now_h + dx[i]
        next_w = now_w + dy[i]
        if not (0 <= next_h <= h-1 and 0 <= next_w <= w-1):
            continue
        if distance[next_h][next_w] == -1:
            distance[next_h][next_w] = now_distance + 1
            queue.append((next_h, next_w))
            ans = now_distance + 1
            # print("appended {} {}".format(next_h, next_w))

print(ans)
