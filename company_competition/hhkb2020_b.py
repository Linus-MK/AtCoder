h, w = list(map(int, input().split()))
ss = []
for i in range(h):
    ss.append(input())

ans = 0

for i in range(h):
    for j in range(w-1):
        if ss[i][j] == ss[i][j+1] == '.':
            ans += 1

for i in range(h-1):
    for j in range(w):
        if ss[i][j] == ss[i+1][j] == '.':
            ans += 1

print(ans)
