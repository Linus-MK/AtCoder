n = int(input())
arr = list(map(int, input().split()))
ans = 0
min_here = 3 * 10 ** 5
for ele in arr:
    if min_here > ele:
        ans += 1
    min_here = min(min_here, ele)
print(ans)