a, b, c = list(map(int, input().split()))

m = max(a, b, c)
s = sum([a, b, c])
if (3 * m - s) % 2 == 0:
    print((3 * m - s) // 2)
else:
    print((3 * m + 3 - s) // 2)