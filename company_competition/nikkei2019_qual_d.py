# 題意としてはよく分かる。
# 有向の根付き木に対してショートカットみたいな辺を張って、
# もとの辺とショートカットの辺はどれか区別せよって問題。

# 有向の根付き木なので、根から葉に探索するか、葉から根に探索するかの2択じゃないかと思った。

# 根から葉でできるのか考える。
# 幅優先探索とかかなぁ?
# A→B→C→D→E とA→Xがあったとして、E→Xが最後に分かればA→Xがショートカットだったんだって分かるわけ。
# でも最後まで分からない。E→Xがなければ正常な木なので。
# 最後にひっくり返る可能性がある
# 0-1 BFSの解説記事 https://betrue12.hateblo.jp/entry/2018/12/08/000020 に出てくる言葉だけど
# 「後からより短い経路が見つかることがあり、その先が全部探索し直しになる」という懸念があり、計算量が上から抑えられない。ダメだ。

# 葉から根だと、「各点の親が1つだけあるのが正常、2つ以上ならおかしい」が確定するのはうれしいけど、
# やっぱり「最後にひっくり返る可能性」があることには変わらなくて辛い。

# 根から葉に進む上で最も移動回数が多くなるものを求めよ、という問題に近いのよ。
# 最短経路問題の逆……
# ……ってことは、辺の重みを全部 -1 にして、負の辺でもできる最短経路問題アルゴリズムを適用すればできる?

# --- 解説見る ---

# あーーーーそうか。このグラフはDAGです、だからトポロジカルソートできます。までは普通に考えられたんだけど
# なぜか「当該頂点の親は、当該頂点に入ってくる枝がある頂点のうち番号最大のものです」まで行けなかった。何でだろう。

# Python, PyPyともAC

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for i in range(n+m-1)] 
neighbor = [[] for i in range(n)]
reverse = [[] for i in range(n)]

in_degree = [0 for i in range(n)]
for e in edges:
    neighbor[e[0] - 1].append(e[1] - 1)
    reverse[e[1] - 1].append(e[0] - 1)
    in_degree[e[1] - 1] += 1
    # 1-index → 0-index

# 幅優先探索によるトポロジカルソート
# https://algo-logic.info/topological-sort/
# 幅優先探索でも深さ優先探索でもできるらしい。計算が早い幅優先探索でやりましょう

from collections import deque
queue = deque()
for i, deg in enumerate(in_degree):
    if deg == 0:
        # 入次数が0なので、トポロジカルソートの始点にできる。今回は1つの頂点しか無いけど、一般には複数
        queue.append(i)

# visited = [False for i in range(n)]
ans = []
position = [-1] * n
present_pos = 0
while len(queue) > 0:
    vertex = queue.popleft()
    ans.append(vertex)
    position[vertex] = present_pos
    present_pos += 1
    for nei in neighbor[vertex]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue.append(nei)
    
for i in range(n):
    if position[i] == 0:
        # 根です
        print(0)
    else:
        ans = -1
        max_pos = -1
        # 当該頂点に入ってくる点全てのうち、位置が最大となるものです
        for vertex in reverse[i]:
            if position[vertex] > max_pos:
                max_pos = position[vertex]
                ans = vertex
        print(ans+1)

