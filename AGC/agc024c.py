# 0, 1, 2, 3, ... の重ね合わせで書けるかどうか。多分。証明してないけど。

n = int(input())

nums = [int(input()) for i in range(n)]

if nums[0] != 0:
    print(-1)
    exit()

ans = 0
for i in range(1, n):
    if nums[i] > nums[i-1] + 1:
        print(-1)
        exit()
    elif nums[i] == nums[i-1] + 1:
        # 直前と同じ山に含まれる
        ans += 1
    else:
        # 直前とは違う、新たな山を作る必要がある
        ans += nums[i]

print(ans)
