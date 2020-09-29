# 最小全域木（mininum spanning tree）の問題

# 頂点、辺どちらの数もO(WH)なので、木を求めるアルゴリズムを直接適用するのは不可能（TLE）。
# 計算の工夫で計算量を減らす。
# クラスカル法（コストの小さい順に、閉路ができないように辺を追加）を用いる。
# 縦向きの辺は、最初はW+1本全てを選択する。「それまで選択された横の辺（の組）」の数だけ減る。その数だけ横がひと繋がりになっているので。
# 横向きの辺は、最初はH+1本全てを選択する。「それまで選択された縦の辺（の組）」の数だけ減る。その数だけ縦がひと繋がりになっているので。
# 縦と横の長さを一緒にしてソートするにはどうする?
# - 縦と横を独立にソートして、どちらが小さいか管理しながら左から見る。尺取り的なやり方。
# - 縦横情報を入れて長さで一緒にソートする。 →こっちが簡単そう。

w, h = list(map(int, input().split()))

yoko = [(int(input()), 'yoko') for _ in range(w)]
tate = [(int(input()), 'tate') for _ in range(h)]

sorted_edge = sorted(yoko + tate, key=lambda x: x[0])

ans = 0
tate_num = 0
yoko_num = 0
for length, direction in sorted_edge:
    if direction == 'tate':
        ans += length * (w + 1 - yoko_num)
        tate_num += 1
    else:
        ans += length * (h + 1 - tate_num)
        yoko_num += 1

print(ans)
