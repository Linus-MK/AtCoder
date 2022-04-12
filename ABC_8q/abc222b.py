n, p = list(map(int, input().split()))
nums = list(map(int, input().split()))

ans = sum([num < p for num in nums])
print(ans)
