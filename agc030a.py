a, b, c = list(map(int, input().split()))
if a + b >= c - 1:
    print(b + c)
else:
    print(a+b+1 + b)
