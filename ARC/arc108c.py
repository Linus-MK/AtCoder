# 構成系、構築系
# 奇数個の辺からなる閉路があって、それにすべて同じラベルがついてたら不可
### じゃなかった。勘違い。

# グラフが木だったら?
# 葉がある辺を選ぶ、葉にその辺のラベルを貼る、後はその辺のことを忘れて良い……とはならないんだよなー。
# 片方だけじゃなきゃいけないから、両方の点が同じラベルだとまずい。
# 一般のグラフでも、グラフから木を取ってきて、その木の辺が全部残ればOK

# 証明：
# グラフは連結なので、グラフの部分木を適当に定める。
# 以下、この木の辺だけを考える。なぜなら、この木の辺がすべて残ればグラフは連結になるからである。
# 適当な点から開始して、幅優先探索をする。
# 対象となる辺に対して、
### すでに探索済みのほうの頂点が辺と違うラベルである→他方の頂点には同じラベルを貼る
### すでに探索済みのほうの頂点が辺と同じラベルである→他方の頂点には違うラベルを貼る
# を繰り返せば良い。
# 以上で、条件を満たす書き込み方が必ず存在することが示された。

# コーディングのときは「部分木を取り出す」と「頂点にラベルを貼り付ける」を同時に実施する。
# これは、すでに通った頂点に行く辺があった場合に無視するようにすれば良い。（多重辺もこうすれば問題ない。）
# なお、探索を葉から開始しなければ行けないかと途中まで思っていたが、そんなことはない。任意の頂点から開始して良い。

# 葉を探そう→不要
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
