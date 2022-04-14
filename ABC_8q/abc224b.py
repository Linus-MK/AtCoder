h, w = list(map(int, input().split()))
masu = []
for i in range(h):
    temp = list(map(int, input().split()))
    masu.append(temp)

ans = 'Yes'
for i1 in range(h):
    for i2 in range(i1+1, h):
        for j1 in range(w):
            for j2 in range(j1+1, w):
                if masu[i1][j1] + masu[i2][j2] <= masu[i1][j2] + masu[i2][j1]:
                    pass
                else:
                    ans = 'No'
print(ans)
