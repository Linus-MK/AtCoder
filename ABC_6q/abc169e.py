n = int(input())

minimum = []
maximum = []
for i in range(n):
    a, b = list(map(int, input().split()))

    minimum.append(a)
    maximum.append(b)

# 奇数の場合は？

minimum.sort()
maximum.sort()

if n % 2 == 1:
    print(maximum[(n+1)//2 - 1]- minimum[(n+1)//2 - 1] + 1)
else:
    upper = maximum[n//2-1] + maximum[n//2]
    lower = minimum[n//2-1] + minimum[n//2]
    print(upper - lower + 1)

