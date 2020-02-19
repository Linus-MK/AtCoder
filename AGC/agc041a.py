n, a, b = list(map(int, input().split()))

if (a-b) % 2 == 0:
    print(abs(a-b)//2)
else:
    x = ((a-1) + (b-1) + 1)//2
    y = ((n-a) + (n-b) + 1)//2
    print(min(x, y))
