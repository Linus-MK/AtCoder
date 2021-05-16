n = int(input())
heights = list(map(int, input().split()))

heights = list(set(heights))
heights.sort()

prev = 0
ans = 1
for h in heights:
    ans *= (h-prev+1)
    ans %= (10**9 +7)
    prev = h


print(ans)
