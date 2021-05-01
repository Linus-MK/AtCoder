# 
# 有向グラフに対する幅優先探索 distanceも必要 AGC068Cからコピーしてきた
# 操作の途中で数がどこまで大きくなるんだろうか……

# 幅優先探索, BFS
from collections import deque

# n, m = list(map(int, input().split()))
# edges = [list(map(int, input().split())) for _ in range(m)]

n = (2**8) * 2 * 2 # 根拠はない 4倍なら大丈夫かなぁ
n = (2**8) * (2**8) # 根拠はない

neighbor = [[] for _ in range(n)]

for i in range(n):
    # n → 2*n
    if 2*i < n:
        neighbor[i].append(2*i)
    
    bit_n = format(i, 'b')
    bit_len = len(bit_n)
    bit_not = (1 << bit_len) - 1 - i
    # print(i, bit_not)
    neighbor[i].append(bit_not)


n_test = int(input())
for i_test in range(n_test):

    start_str, end_str = input().split()
    start = int(start_str, 2)
    end = int(end_str, 2)
    if start > 255 or end > 255:
        exit()

    inf = 10 ** 5
    distance = [inf] * n

    queue = deque()
    queue.append(start)
    distance[start] = 0
    while len(queue) > 0:
        vertex = queue.popleft()
        for nei in neighbor[vertex]:
            if distance[nei] == inf:
                distance[nei] = distance[vertex] + 1
                queue.append(nei)

    if distance[end] < inf:
        ans = distance[end]
    else:
        ans = 'IMPOSSIBLE'

    print("Case #{0}: {1}".format(i_test+1, ans))
