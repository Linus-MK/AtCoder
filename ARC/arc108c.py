# 構成系、構築系
# 奇数個の辺からなる閉路があって、それにすべて同じラベルがついてたら不可
### じゃなかった。勘違い

# グラフが木だったら?
# 葉がある辺を選ぶ、葉にその辺のラベルを貼る、後はその辺のことを忘れて良い……とはならないんだよなー。
# 片方だけじゃなきゃいけないから両方の点が同じラベルだとまずい。
# 一般のグラフでも、グラフから木を取ってきて、その木の辺が全部残ればOK

# 葉を探そう
# 幅優先探索, BFS
from collections import deque

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0]-1].append((edge[1]-1, edge[2]))  # 1- → 0-index
    neighbor[edge[1]-1].append((edge[0]-1, edge[2]))

vertex_label = [-1] * n
ans = 1

queue = deque()
queue.append(0)
vertex_label[0] = 1  # 適当に値を決める
while len(queue) > 0:
    vertex = queue.popleft()
    for nei, edge_label in neighbor[vertex]:
        if vertex_label[nei] == -1:
            if edge_label != vertex_label[vertex]:
                vertex_label[nei] = edge_label
            else:
                # vertex_label[nei] != edge_label になるようにvertex_label[nei]を定める
                if edge_label == 1:
                    vertex_label[nei] = 2
                else:
                    vertex_label[nei] = 1
            queue.append(nei)
    
for label in vertex_label:
    print(label)
