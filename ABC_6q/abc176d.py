# 1マス移動するごとに周囲5*5を見て現在+1を書き込む? ◎
# それとも移動できるまで移動してから、次を探しに行く?
# 幅優先か、深さ優先か? 幅優先

# AGC033Aからコピペ

h, w = list(map(int, input().split()))

start = list(map(int, input().split()))
goal = list(map(int, input().split()))

masu = [input() for i in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

inf = 10 ** 7
distance = [[inf for _ in range(w)] for _ in range(h)]

from collections import deque

queue = deque([])
distance[start[0]-1][start[1]-1] = 0
queue.append((start[0]-1, start[1]-1, 0))

while True:
    if len(queue) == 0:
        break
    now = queue.popleft()
    now_h = now[0]
    now_w = now[1]
    now_distance = now[2]
    now_distance_matrix = distance[now_h][now_w]

    if now_distance > now_distance_matrix:
        # もう小さい数字がdistanceに書かれているので
        continue
    distance[now_h][now_w] = now_distance

    for hh in range(now_h - 2, now_h + 2+1):
        for ww in range(now_w - 2, now_w + 2+1):
            if not (0 <= hh <= h-1 and 0 <= ww <= w-1):
                continue
            if masu[hh][ww] == '#':
                continue
            if distance[hh][ww] <= now_distance:  # ここで統合を入れるべきか否か全く自信がない 1
                continue
            queue.append((hh, ww, now_distance + 1))

    for i in range(4):
        next_h = now_h + dx[i]
        next_w = now_w + dy[i]
        if not (0 <= next_h <= h-1 and 0 <= next_w <= w-1):
            continue
        if masu[next_h][next_w] == '#':
            continue
        if distance[next_h][next_w] <= now_distance:  # ここで統合を入れるべきか否か全く自信がない 2
            continue
        else:
            distance[next_h][next_w] = now_distance
            queue.appendleft((next_h, next_w, now_distance))

t = distance[goal[0]-1][goal[1]-1]
if t == inf:
    print(-1)
else:
    print(t)

# print(distance)
