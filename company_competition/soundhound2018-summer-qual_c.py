n, m, d = list(map(int, input().split()))
t = (n-d) * 2 *(m-1) / (n ** 2)
if d == 0:
    print(t/2)
else:
    print(t)
