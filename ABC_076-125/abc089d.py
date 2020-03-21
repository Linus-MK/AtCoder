# クエリが何回か飛んでくる→累積和か?

# 1回の実技試験での最大移動回数は、H*W/1 = 90000→愚直に計算すると無理。

# Dが実技試験によらず一定なので、移動後のマスから移動前のマスは分かる。

# 最初に各マスについて座標を調べて
# 次に移動前のマスとのマンハッタン距離を調べる
# しかし毎回の試験の魔力を愚直に計算すると、やはり90000程度が掛かって無理。

# P_i = i%Dからiまで移動して来るのに必要な魔力（i<=Dなら0）
# とすれば、毎回のクエリにはP_R - P_Lを出せばよく、定数時間で求まる


masu = h * w
x_coord = [-1] * masu
y_coord = [-1] * masu

distance_sum = [0] * sum
for i in masu:
    if i < d:
        pass
    else:
        distance_sum[i] = distance_sum[i-d] + abs(x_coord[1] - x_coord[1]) + abs(y_coord[1] - y_coord[1])