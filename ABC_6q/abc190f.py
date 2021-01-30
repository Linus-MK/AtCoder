# F chokudai speedrun 1 I をコピーして転倒数（反転数）が出る。
# あとは最初の数を最後に移動するので、その時の変動が計算できる。順次計算すれば良い。

# （最初は、長さ2Nの列からBITを作るのか?とか考えてしまった）
# BITを使うときは添字を1始まりにする必要があるっぽい

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
