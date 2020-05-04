n, k = list(map(int, input().split()))

have_candy = [False] * n
for i in range(k):
    d = int(input())
    x = list(map(int, input().split()))
    for i in x:
        have_candy[i-1] = True

print(n - sum(have_candy))
