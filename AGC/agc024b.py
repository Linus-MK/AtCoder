# 同じ数を2回以上移動するのは無駄。最後の1回だけやればいいから。
# したがって全ての数は移動が0回または1回になる。
# 移動しない数はそのままの並び順になる。
# 逆に言えば、連続する数値からなる部分列の最長のものを見つければ、それ以外の数を移動させればよい。
# 例2では「3, 4」または「5, 6」が該当する。
# ではそれをどうやって見つけるか?
# 各数の位置を格納した配列を作る（1の位置を探して、2の位置を……とやるとO(N^2)でダメ。数列の先頭から順にやる）
# その配列を順に舐めて最大単調増加部分を見つければ良い

n = int(input())
posi = [-1] * n  # posi[i-1]には、数iの場所が0-indexで入る。

for k in range(n):
    temp = int(input())
    posi[temp - 1] = k - 1

temp = 1
maxx = 0
for i in range(n-1):
    if posi[i] < posi[i+1]:
        temp += 1
    else:
        maxx = max(maxx, temp)
        temp = 1

maxx = max(maxx, temp)

print(n - maxx)
