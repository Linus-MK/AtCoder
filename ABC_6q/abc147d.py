# 和を求める問題を見たら、足し算の順序を変えて高速に計算できないか考えよ の典型例ですね。
# 各ビットごとに、「0の個数」×「1の個数」だけXORが1になるので、その和を取れば良い。

n = int(input())
nums = list(map(int, input().split()))

bitcount = [[0 for _ in range(2)] for _ in range(60)]

for idx in range(60):
    for num in nums:
        if num & (1 << idx):
            bitcount[idx][1] += 1
        else:
            bitcount[idx][0] += 1

ans = 0
for idx in range(60):
    ans += (1 << idx) * bitcount[idx][0] * bitcount[idx][1]
    ans %= (10**9 + 7)
 
print(ans)
