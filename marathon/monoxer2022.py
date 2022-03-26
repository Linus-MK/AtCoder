import random
random.seed(0)

sr, sc, tr, tc, prob = input().split()
sr = int(sr)
sc = int(sc)
tr = int(tr)
tc = int(tc)
hori_wall = []
for i in range(20):
    hori_wall.append(input())

vart_wall = []
for i in range(19):
    vart_wall.append(input())

ans = 'DR' * 60
# 進めなくなったときに脱出
for i in range(1, 7):
    # ans[i*8] = 'U'  # Dの代わりにU
    # ans[i*8 + 5] = 'L'  # Rの代わりにL
    ans = ans[:i*16 - 1] + 'U' + ans[i*16:]  # Dの代わりにU
    ans = ans[:i*16 + 6] + 'L' + ans[i*16 + 7:] # Rの代わりにL

row = 19
col = 19

from collections import deque

queue = deque()
queue.append((19, 19, 'U', ''))
queue.append((19, 19, 'L', ''))

reach = False
while len(queue) > 0:
    vertex = queue.popleft()
    # 移動を試みる
    row = vertex[0]
    col = vertex[1]
    dire = vertex[2]
    traj = vertex[3]
    
    if row == tr and col == tc:
        reach = True
        break
    if dire == 'U':
        if row <= 10:
            pass
        if vart_wall[row-1][col] == '1':
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        else:
            queue.append((row-1, col, 'U', traj+'U'))
    if dire == 'D':
        if row == 19:
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        if vart_wall[row][col] == '1':
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        else:
            queue.append((row+1, col, 'D', traj+'D'))
    if dire == 'L':
        if col <= 10:
            pass
        print(row, col)
        if hori_wall[row-1][col-1] == '1':
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        else:
            queue.append((row, col-1, 'L', traj+'L'))
    if dire == 'R':
        if col == 19:
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        if hori_wall[row][col-1] == '1':
            queue.append((row, col, 'L', traj))
            queue.append((row, col, 'R', traj))
        else:
            queue.append((row, col+1, 'R', traj+'R'))

if reach:
    for ch in traj:
        ans += ch
        ans += ch

    ans = ans[:200]
else:

    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[3, 3, 1, 1], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[1, 1, 3, 3], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[3, 3, 1, 1], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[1, 1, 3, 3], k=20)
    ans += ''.join(ch_list)
print(ans)
