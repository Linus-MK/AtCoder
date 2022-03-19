n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

for i in range(n):
    start[i] = start[i] + i
    end[i] = end[i] + i

s_start = sorted(start)
s_end = sorted(end)

for i in range(n):
    if s_start[i] != s_end[i]:
        print(-1)
        exit()

occur = {}
for i in range(n):
    curr = occur.get(start[i] , 0)
    occur[start[i]] = curr + 1
    if curr > 0:
        start[i] += (curr * 10 ** 10)

occur = {}
for i in range(n):
    curr = occur.get(end[i] , 0)
    occur[end[i]] = curr + 1
    if curr > 0:
        end[i] += (curr * 10 ** 10)

mydict = {}

for idx in range(n):
    mydict[end[idx]] = idx

idx_list = [0] * n
for idx in range(n):
    idx_list[idx] = mydict[start[idx]] + 1


# 転倒数。蟻本のp.162に全く同一の問題あり。ここでは反転数という名称。

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
    # ans += idx_list内で現在より左側の位置にあり、現在の数より大きい要素の個数。
    # これは、j - 配列[0:現在の数] に等しい
    ans += j - calc_sum(idx_list[j])
    add(idx_list[j], 1)

print(ans)
