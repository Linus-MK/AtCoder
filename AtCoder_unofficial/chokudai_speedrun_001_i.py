n = int(input())
nums = list(map(int, input().split()))

# 累積和 + α
# 累積和が単調増加であることを利用して二分探索で解くか(NlogN)
# 1からの相異なる数の和がnに達するのは割と早いことを利用して逐次計算で解くか(最悪N√Nだがそれより小さいはず)
# 後者でやってみよう
# 369ms, 余裕を持って間に合う

cumsum = [0] * (n+1)

for i in range(n):
    cumsum[i+1] = cumsum[i] + nums[i]

ans = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if cumsum[j] - cumsum[i] == n:
            ans += 1
        elif cumsum[j] - cumsum[i] > n:
            break

print(ans)
