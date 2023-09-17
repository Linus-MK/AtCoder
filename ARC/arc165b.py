# 操作で変わらないならそれが最善
# 基本的に一番後ろを採用。ただ n-k+1から左に見ていき、単調減少が止まったところまで戻る

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

# 操作で変わらないならそれが最善
increase = 0
max_inc = 0
for i in range(n-1):
    if nums[i] < nums[i+1]:
        increase += 1
    else:
        max_inc = max(max_inc, increase)
        increase = 0

if max_inc >= k-1:
    ans_str = list(map(str, nums))
    print(" ".join(ans_str))
    exit(0)


right = n-k
idx = right
for i in range(right, 0, -1):
    if nums[i-1] < nums[i]:
        idx -= 1
    else:
        break


ans = nums[:idx] + sorted(nums[idx: idx+k]) + nums[idx+k:]
ans_str = list(map(str, ans))
print(" ".join(ans_str))
