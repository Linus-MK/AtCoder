n = int(input())
arr = list(map(int, input().split()))

count = 1
ans = 0
for i in range(1, n):
    if arr[i] == arr[i-1]:
        count += 1
    else:
        ans += count // 2
        count = 1

ans += count // 2
print(ans)
