# 「1つ前にどこを訪問したかも管理するタイプの幅優先探索か？えーっと洞窟の出口に移動する問題があったよな」で
# ABC168 D （.. (Double Dots) ）をコピペして修正してなんとかした。

# 幅優先探索はキューに入れるタイミングと取り出すタイミングと訪問済みか判定するタイミングがうまく整合しないと
# 無限にバグらせてしまうことがある。今回もその傾向がある。
# ABC184E（Third Avenue）を自主練で解いたときも、だいぶやらかした。

# 幅優先探索, BFS

from collections import deque

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]

vertex_num = 200000*2
neighbor = [[] for _ in range(vertex_num)]
for edge in edges:
    neighbor[edge[0]-1].append(edge[1]-1)  # 1- → 0-index
    neighbor[edge[1]-1].append(edge[0]-1)

queue = deque()

back = [-1] * vertex_num  # visitしたかどうかを兼ねる
ans = 0

for i in range(vertex_num):
    if back[i] == -1 and neighbor[i]:

        queue.append(i)
        back[i] = i
        ans += 1

        contain_loop = False
        while len(queue) > 0:
            vertex = queue.popleft()
            for nei in neighbor[vertex]:
                if nei == vertex:
                    # 自己辺
                    contain_loop = True
                if back[nei] == -1:
                    back[nei] = vertex
                    queue.append(nei)
                    ans += 1
                else:
                    if nei != back[vertex]:
                        # 1つ前がすでに決まっている：閉路を含む
                        contain_loop = True

        if not contain_loop:
            ans -= 1

print(ans)
