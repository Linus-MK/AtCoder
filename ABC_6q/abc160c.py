k, n = list(map(int, input().split()))
positions = list(map(int, input().split()))

diffs = [-1] * (n)
for i in range(n-1):
    diffs[i] = positions[i+1] - positions[i]
diffs[n-1] = positions[0] - positions[-1] + k

print(k - max(diffs))
