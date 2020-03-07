# 幅優先探索か深さ優先探索で、上下左右の隣接と異なる色ならば、連続する1つの領域とする
# 各領域ごとに、白マス数×黒マス数を計算し、その合計が答え

h, w = list(map(int, input().split()))
masu = [input() for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# とりあえず周囲の番兵は使わずに書いてみよう……

# 再帰関数の呼び出し回数が多くなる時はこれが必要！！無いとruntime errorになる。
import sys
sys.setrecursionlimit(400*400 + 10)

def dfs(hi, wi, white, black):
    global colors
    global dx, dy
    global visited

    # print(hi, wi)

    visited[hi][wi] = True
    if masu[hi][wi] == '.':
        white += 1
    if masu[hi][wi] == '#':
        black += 1

    for neighbor in zip(dx, dy):
        h_new = hi + neighbor[0]
        w_new = wi + neighbor[1]
        # print("new: " , h_new, w_new)
        if 0 <= h_new <= h-1 and 0 <= w_new <= w-1:
            if not visited[h_new][w_new]:
                if masu[hi][wi] != masu[h_new][w_new]:
                    white, black = dfs(h_new, w_new, white, black)
    
    return white, black

ans = 0
for hi in range(h):
    for wi in range(w):
        if not visited[hi][wi]:
            white, black = dfs(hi, wi, 0, 0)
            ans += white * black

print(ans)
