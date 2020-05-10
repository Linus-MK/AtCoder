# もしかして：こるとんさん作

n, m, x = list(map(int, input().split()))

price = []
a = []

for i in range(n):
    arr = list(map(int, input().split()))
    price.append(arr[0])
    a.append(arr[1:])

ans = 10 ** 10
for num in range(2 ** n):
    rikaido = [0] * m
    cost = 0
    for i in range(n):
        # i冊目を買うか
        buy = num & (1 << i) > 0
        if buy:
            for j in range(m):
                rikaido[j] += a[i][j]
            cost += price[i]
    
    target = True
    # 条件を満たすか
    for j in range(m):
        if rikaido[j] < x:
            target = False
    
    if target:
        ans = min(cost, ans)

if ans == 10 ** 10:
    ans = -1
print(ans)

