n, x = list(map(int, input().split()))
nums = list(map(int, input().split()))

ans = 1
known = [False] * n
known[x-1] = True

cur = x-1
while True:
    next_ = nums[cur] - 1
    if known[next_]:
        break
    else:
        known[next_] = True
        ans += 1
        cur = next_

print(ans)
