n, m = list(map(int, input().split()))

if m == 0:
    print(1)
    exit()

if n == m:
    print(0)
    exit()

nums = list(map(int, input().split()))
nums.append(0)
nums.append(n+1)
nums.sort()

diff = [nums[i+1] - nums[i] - 1 for i in range(m+1)]
diff = [d for d in diff if d > 0]

unit = min(diff)
ans = sum([(a+unit-1)//unit for a in diff])
print(ans)
