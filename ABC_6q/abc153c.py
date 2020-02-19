arr = list(map(int, input().split()))
arr.sort()
k = min(n, k)
print(sum(arr[:n-k]))
