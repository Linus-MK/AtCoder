n, a, x, y = list(map(int, input().split()))
if n <= a:
    print(x*n)
else:
    print(x*n-(x-y)*(n-a))
