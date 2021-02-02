n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

ans = 'No'
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (coords[i][1] - coords[j][1]) * (coords[i][0] - coords[k][0]) \
                == (coords[i][1] - coords[k][1]) * (coords[i][0] - coords[j][0]):
                ans = 'Yes'

print(ans)
