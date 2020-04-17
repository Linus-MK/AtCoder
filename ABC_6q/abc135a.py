a, b = list(map(int, input().split()))
if (a-b) % 2:
    print('IMPOSSIBLE')
else:
    print((a+b)//2)
