# 二通りのやり方で解いてみよう。
# Aそれぞれに対してBを二分探索→M(累積和構成) + NlogM このコードはこっち★ 310ms
# Aを昇順、Bを降順に動かす→O(N+M)

import bisect

n, m, k = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

# 累積和を作る
b_cumsum = [0] * (m+1)
for i in range(m):
    b_cumsum[i+1] = b_cumsum[i] + bb[i]

ans = 0
a_sum = 0
b_rest = k

temp = bisect.bisect(b_cumsum, b_rest) - 1
ans = max(ans, temp)

for idx, a in enumerate(aa):
    a_sum += a
    b_rest -= a
    if a_sum > k:
        break
    temp = idx + 1 + bisect.bisect(b_cumsum, b_rest) - 1
    ans = max(ans, temp)

print(ans)
