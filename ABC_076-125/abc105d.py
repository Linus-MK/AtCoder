# 解説見てAC
# 愚直解法 = O(N^3)でTLE
# 累積和を入れても、O(N^2)でTLE

# S_k をA_1からA_kまでの和として
# 条件を満たす←→S_(l-1)とS_rをMで割ったあまりが等しい
# Mが十分大きいので、Mで割った余りを配列で取るのはダメ、平衡二分木かハッシュマップ（辞書、dict）を使う

n_box, kids = list(map(int, input().split()))
nums = list(map(int, input().split()))

residue_num = {}
residue_num[0] = 1  # S_0のぶん
summ = 0
for i in range(n_box):
    summ += nums[i]
    r = summ % kids
    residue_num[r] = residue_num.get(r, 0) + 1

ans = 0
for i in residue_num.values():
    ans += i * (i-1) // 2

print(ans)
