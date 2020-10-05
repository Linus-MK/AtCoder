# 条件は「A_lからA_rまでの間に、全てのビットで重複が無い（1個以下の数）」と言い換えられる。
# しかしこれを二重for文で回すとO(N^2)となってしまう。単純に条件をそのまま計算するのと変わらない。
# lに対してrの範囲を二分探索すればO(NlogN)
# xor <= sum なので、 <か=かで判定すれば良い
# なお累積ORは不適切。途中からの累積が取れないので。
# 累積XORのほうが累積ORよりも好ましい性質を持ってるから、XORを使う方が良いんだね。

# 公式解説は尺取り法でO(N)でした。
# **lを1増やしたときにrが減ることはなく、同じか増加する→尺取り法が使える**

n = int(input())
nums = list(map(int, input().split()))

# cumsum[i] はi番目までの和 特にcumsum[0]は空集合の和なので0
cumsum = [0 for i in range(n+1)]
for i in range(n):
    cumsum[i+1] = cumsum[i] + nums[i]


# cumxor[i] はi番目までのxor 特にcumxor[0]は空集合のxorで、単位元0とする
cumxor = [0 for i in range(n+1)]
for i in range(n):
    cumxor[i+1] = cumxor[i] ^ nums[i]

ans = 0
for start in range(n):
    # めぐる式二分探索 ok < ngの場合でも全く同様に書ける
    end_ok = start+1 # 1要素からなる集合は明らかに条件を満たす
    end_ng = n+1 # nも条件を満たす場合がある（全て0の場合など）。n+1を実際に試すことはないので範囲外参照にはならない

    while abs(end_ok - end_ng) > 1:
        mid = (end_ok + end_ng) // 2
        if cumsum[mid] - cumsum[start] == cumxor[mid] ^ cumxor[start] :
            end_ok = mid
        else:
            end_ng = mid
        
    # start+1, start+2, ..., end_ok を加算
    ans += (end_ok - (start+1) + 1)

print(ans)
