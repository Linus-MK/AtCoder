n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if -1 <= (coords[j][1] - coords[i][1]) / (coords[j][0] - coords[i][0]) <= 1:
            ans += 1
print(ans)
