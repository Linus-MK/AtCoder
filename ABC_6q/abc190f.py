n = int(input())
nums_orig = list(map(int, input().split()))
nums = [i+1 for i in nums_orig]

# 蟻本のp.162に全く同一の問題あり。ここでは反転数という名称。

# Binary Indexed Tree = BIT

bit = [0] * (n+1)


def calc_sum(i):
    s = 0
    while (i > 0):
        s += bit[i]
        i -= i & -i
    return s


def add(idx, num):
    while (idx <= n):
        bit[idx] += num
        idx += idx & -idx


ans = 0
for j in range(n):
    # ans += nums内で現在より左側の位置にあり、現在の数より大きい要素の個数。
    # これは、j - 配列[0:現在の数] に等しい
    ans += j - calc_sum(nums[j])
    add(nums[j], 1)

print(ans)

for i in range(n-1):
    num = nums_orig[i]
    ans += (n-1 - 2*num)
    print(ans)
    