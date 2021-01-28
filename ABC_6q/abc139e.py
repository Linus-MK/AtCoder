# それぞれの試合を頂点とするグラフを考える。
# 例えば選手1が選手3→2→4の順で試合をする場合、
# (1, 3)→(1, 2)と(1, 2)→(1, 4)に有向辺を張る。
# 「節約」して、隣接する関係だけに辺を張っても特に問題ない気がする。この例だと(1, 3)→(1, 4)は要らないと思う。
# ……上記の証明は自明ではないが飛ばしてしまおう。

# で、これがDAGになるか（=トポロジカルソートできるか）を判定する。
# トポロジカルソートできないなら、無理。日程の前後関係を無矛盾に配置することはできない。
# トポロジカルソートできるなら、最小日数を考えよう。
# 辺で結ばれている場合、同じ日程にできない。
# 辺で結ばれていない場合、同じ日程にできる。
# 「辺で結ばれている」点がつながっていると、その分日数が必要だ……DAGの最長経路長の長さが答えだ！

# 公式解説は深さ優先探索でできるよって書いてある。やだ。深さ優先探索でやりたくない。幅優先探索でやりたい。
# 幅優先探索しながら走査、入次数が0のものが取れなくなったら次の日の試合だから、カウントを1増やす、をすればよい。

n_people = int(input())
n = n_people * (n_people - 1) // 2
# n, m = list(map(int, input().split()))
matches = [list(map(int, input().split())) for i in range(n_people)]
# edges = [list(map(int, input().split())) for i in range(n+m-1)] 
neighbor = [[] for i in range(n)]
reverse = [[] for i in range(n)]

def calc_edge_idx(i, j):
    # 引数は0-index
    # (1, 0)→0
    # (2, 0)→1
    # (2, 1)→2 ...
    if i < j:
        i, j = j, i
    return ((i-1) * i) // 2 + j

in_degree = [0 for i in range(n)]

for i, m in enumerate(matches):
    for relation_i in range(n_people-2):
        idx_before = calc_edge_idx(i, m[relation_i] - 1)  # 1-index → 0-index
        idx_after = calc_edge_idx(i, m[relation_i+1] - 1)
    
        neighbor[idx_before].append(idx_after)
        reverse[idx_after].append(idx_before)
        in_degree[idx_after] += 1

# 幅優先探索によるトポロジカルソート
# https://algo-logic.info/topological-sort/
# 幅優先探索でも深さ優先探索でもできるらしい。計算が早い幅優先探索でやりましょう

# print(neighbor)
# print(in_degree)

from collections import deque
queue = deque()
queue2 = deque()
# キューに入れる際に、一回別のキューにし、もとのキューが空になったところで次の日に移動する。キューのコピーが発生するから重くなるけど
for i, deg in enumerate(in_degree):
    if deg == 0:
        # 入次数が0なので、トポロジカルソートの始点にできる。
        queue.append(i)

topological_sorted = []  # 実は今回は不要
position = [-1] * n
present_pos = 0
ans = 1
while len(queue) > 0:
    vertex = queue.popleft()
    topological_sorted.append(vertex)
    position[vertex] = present_pos
    present_pos += 1
    for nei in neighbor[vertex]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue2.append(nei)
    if len(queue) == 0 and len(queue2) > 0:
        queue = queue2.copy()
        queue2 = deque()
        ans += 1
    
if present_pos < n:
    # 入次数が0の点が途中で無くなった = トポロジカルソートできない
    print(-1)
else:
    print(ans)
