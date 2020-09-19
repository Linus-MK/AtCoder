n = int(input())

count = 0
ans = 'No'
for i in range(n):
    p, q =list(map(int, input().split()))
    if p == q:
        count += 1
    else:
        count = 0
    if count >= 3:
        ans = 'Yes'

print(ans)
