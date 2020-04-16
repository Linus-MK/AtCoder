
# 直感的に分かる貪欲（下から組を作る）だと思うんだけど、これでdiff1185は数字が高すぎじゃない? 

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = 0
for idx, m in enumerate(nums):
    if m > 0:
        ans += m // 2
        # m -= (m // 2) * 2
        m = m & 1
    if m == 1 and idx != n-1 and nums[idx+1] >= 1:
        ans += 1
        m -= 1
        nums[idx+1] -= 1

print(ans)
