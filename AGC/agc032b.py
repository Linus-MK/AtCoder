# 完全グラフを考える。
# 隣接する頂点の番号の値は、1〜Nの和から自分自身を引いたもの。

# →奇数の場合は、7ならば1-6, 2-5, 3-4の辺を削除する
# →偶数の場合は、6ならば同上

n = int(input())
if n % 2 == 0:
    excluded_sum = n+1
else:
    excluded_sum = n

print(n*(n-1) // 2 - (excluded_sum-1) // 2)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i+j == excluded_sum:
            continue
        else:
            print('{} {}'.format(i, j))
