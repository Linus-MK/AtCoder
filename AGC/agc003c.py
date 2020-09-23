# パリティ（偶数番目奇数番目)、不変量の問題
# この形のバブルソートもどきは2018年のGCJ予選にも出てたな…… 
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb
# 数3つの入れ替えに寄って、偶数番目と奇数番目は不変なので
# ソートされた状態と元の数列とで偶数番目・奇数番目が異なる要素数 / 2が答え。
# 元の数が全て相異なるのがポイント。

n = int(input())
nums = [int(input()) for _ in range(n)]

sorted_nums = sorted(nums)

nums_idx = {}
for idx, num in enumerate(nums):
    nums_idx[num] = idx

sorted_nums_idx = {}
for idx, num in enumerate(sorted_nums):
    sorted_nums_idx[num] = idx

ans = 0
for num in sorted_nums:
    if (nums_idx[num] - sorted_nums_idx[num]) % 2 :
        ans += 1

print(ans // 2)
