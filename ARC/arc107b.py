n, k = list(map(int, input().split()))

def func(a):
    if 2 <= a <= n+1:
        return a-1
    else:
        return 2*n - a + 1

ans = 0
for i in range(2, 2*n+1):
    ab = i
    cd = i - k
    if 2 <= cd <= 2*n:
        ans += func(ab) * func(cd)
        # print(cd, func(ab), func(cd))

print(ans)
