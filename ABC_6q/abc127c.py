n, m = list(map(int, input().split()))

left = 1
right = n
for i in range(m):
    l, r = list(map(int, input().split()))
    left = max(l, left)
    right = min(r, right)

if left > right:
    print(0)
else:
    print(right - left + 1)
