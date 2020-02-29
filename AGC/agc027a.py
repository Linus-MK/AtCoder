n, candy = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()

ans = 0
for i in range(n):
    if candy >= nums[i]:
        candy -= nums[i]
        ans += 1
    else:
        break

# 配りきってまだ余っている場合
if candy > 0 and ans == n:
    ans -= 1
print(ans)
