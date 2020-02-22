# これを使って解いた問題：
# ABC078-D

# ワーシャル・フロイド法
# 負の辺があっても動作する
# すべての2頂点間の最短路を一気に求められる（ベルマン・フォード、ダイクストラは始点を1つ固定）
# 計算量はループから明らかなように、O(V^3)
# 実装がかんたんなため、計算量に余裕があれば、単一始点最短路問題でもワーシャル・フロイド法を使うとよい（蟻本p.98）


def warshall_floyd(distance, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
