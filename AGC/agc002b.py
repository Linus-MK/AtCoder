n, m = list(map(int, input().split()))

moves = [list(map(int, input().split())) for i in range(m)]

possibilities = [False] * n
possibilities[0] = True
nums = [1] * n

for i in range(m):
    x = moves[i][0] - 1
    y = moves[i][1] - 1

    if possibilities[x]:
        possibilities[y] = True

    nums[x] -= 1
    nums[y] += 1
    if nums[x] == 0:
        possibilities[x] = False

ans = 0
for j in range(n):
    if possibilities[j]:
        ans += 1
print(ans)

