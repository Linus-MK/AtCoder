# 愚直にやると間に合わないので、A_i の取りうる数が少ないことを利用して計算量を落とす

n = int(input())
nums = list(map(int, input().split()))

d = dict()
for num in nums:
    d[num] = d.get(num, 0) + 1

keys = list(d.keys())
ans = 0
for i in range(len(keys)):
    for j in range(i, len(keys)):
        ans += d[keys[i]] * d[keys[j]] * (keys[i] - keys[j]) ** 2
print(ans)
