n, x = list(map(int, input().split()))

# 全通り探索すると2^100 = 10^30になって死亡。
# 1〜10000のマス目を使うDPで100×10000が想定解でしょう。が、setで解いてみよう。

possible_pos = set([0])
for i in range(n):
    a, b = list(map(int, input().split()))
    # pos_a = set([p+a for p in possible_pos])
    # pos_b = set([p+b for p in possible_pos])
    # と書かなくても、setの内包表記がある
    pos_a = {p+a for p in possible_pos}
    pos_b = {p+b for p in possible_pos}
    possible_pos = pos_a | pos_b

if x in possible_pos:
    print("Yes")
else:
    print("No")
