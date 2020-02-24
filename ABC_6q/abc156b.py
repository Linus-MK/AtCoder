n, base = list(map(int, input().split()))

for i in range(100):
    if base ** i <= n < base ** (i+1):
        print(i+1)
        exit()
    